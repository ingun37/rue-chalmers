cmake_minimum_required(VERSION 4.3)
project(clibproj C)

set(CMAKE_C_STANDARD 23)

add_library(clibproj STATIC library.c)
