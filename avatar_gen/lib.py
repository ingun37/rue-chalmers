from dataclasses import dataclass, field
from pathlib import Path

import anny
import torch
import trimesh


@dataclass(frozen=True)
class Avatar:
    seed: int
    model: anny.Anny | None = field(default=None, compare=False, repr=False)


def generate_avatar(seed):
    return Avatar(seed=seed, model=anny.Anny())


def save_avatar(avatar, path):
    if avatar.model is None:
        raise ValueError("avatar does not contain an Anny model")

    available_formats = set(trimesh.available_formats())
    file_type = 'glb'

    if file_type not in available_formats:
        raise ValueError(f"glb format is not available")

    output_path = Path(path).with_suffix(f".{file_type}")

    with torch.no_grad():
        output = avatar.model()

    mesh = trimesh.Trimesh(
        vertices=output["vertices"].squeeze(dim=0).detach().cpu().numpy(),
        faces=avatar.model.faces.detach().cpu().numpy(),
        process=False,
    )
    mesh.export(output_path, file_type=file_type)
    return output_path
