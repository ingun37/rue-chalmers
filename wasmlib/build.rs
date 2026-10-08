fn main() {
    let dst = cmake::Config::new("clibproj")
        .define("CMAKE_TRY_COMPILE_TARGET_TYPE", "STATIC_LIBRARY")
        .build_target("clibproj")
        .build();

    println!("cargo:rustc-link-search=native={}/build", dst.display());
    println!("cargo:rustc-link-lib=static=clibproj");
}
