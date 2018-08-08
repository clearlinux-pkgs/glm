#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : glm
Version  : 0.9.9.0
Release  : 1
URL      : https://github.com/g-truc/glm/releases/download/0.9.9.0/glm-0.9.9.0.zip
Source0  : https://github.com/g-truc/glm/releases/download/0.9.9.0/glm-0.9.9.0.zip
Summary  : OpenGL Mathematics
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-cmake

%description
![glm](/doc/manual/logo-mini.png)
[OpenGL Mathematics](http://glm.g-truc.net/) (*GLM*) is a header only C++ mathematics library for graphics software based on the [OpenGL Shading Language (GLSL) specifications](https://www.opengl.org/registry/doc/GLSLangSpec.4.50.diff.pdf).

%package dev
Summary: dev components for the glm package.
Group: Development
Provides: glm-devel

%description dev
dev components for the glm package.


%prep
%setup -q -n glm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533740178
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd clr-build ; make test ; popd

%install
export SOURCE_DATE_EPOCH=1533740178
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/glm/CMakeLists.txt
/usr/include/glm/common.hpp
/usr/include/glm/detail/_features.hpp
/usr/include/glm/detail/_fixes.hpp
/usr/include/glm/detail/_noise.hpp
/usr/include/glm/detail/_swizzle.hpp
/usr/include/glm/detail/_swizzle_func.hpp
/usr/include/glm/detail/_vectorize.hpp
/usr/include/glm/detail/compute_vector_relational.hpp
/usr/include/glm/detail/dummy.cpp
/usr/include/glm/detail/func_common.inl
/usr/include/glm/detail/func_common_simd.inl
/usr/include/glm/detail/func_exponential.inl
/usr/include/glm/detail/func_exponential_simd.inl
/usr/include/glm/detail/func_geometric.inl
/usr/include/glm/detail/func_geometric_simd.inl
/usr/include/glm/detail/func_integer.inl
/usr/include/glm/detail/func_integer_simd.inl
/usr/include/glm/detail/func_matrix.inl
/usr/include/glm/detail/func_matrix_simd.inl
/usr/include/glm/detail/func_packing.inl
/usr/include/glm/detail/func_packing_simd.inl
/usr/include/glm/detail/func_trigonometric.inl
/usr/include/glm/detail/func_trigonometric_simd.inl
/usr/include/glm/detail/func_vector_relational.inl
/usr/include/glm/detail/func_vector_relational_simd.inl
/usr/include/glm/detail/glm.cpp
/usr/include/glm/detail/qualifier.hpp
/usr/include/glm/detail/setup.hpp
/usr/include/glm/detail/type_float.hpp
/usr/include/glm/detail/type_gentype.hpp
/usr/include/glm/detail/type_gentype.inl
/usr/include/glm/detail/type_half.hpp
/usr/include/glm/detail/type_half.inl
/usr/include/glm/detail/type_int.hpp
/usr/include/glm/detail/type_mat.hpp
/usr/include/glm/detail/type_mat.inl
/usr/include/glm/detail/type_mat2x2.hpp
/usr/include/glm/detail/type_mat2x2.inl
/usr/include/glm/detail/type_mat2x3.hpp
/usr/include/glm/detail/type_mat2x3.inl
/usr/include/glm/detail/type_mat2x4.hpp
/usr/include/glm/detail/type_mat2x4.inl
/usr/include/glm/detail/type_mat3x2.hpp
/usr/include/glm/detail/type_mat3x2.inl
/usr/include/glm/detail/type_mat3x3.hpp
/usr/include/glm/detail/type_mat3x3.inl
/usr/include/glm/detail/type_mat3x4.hpp
/usr/include/glm/detail/type_mat3x4.inl
/usr/include/glm/detail/type_mat4x2.hpp
/usr/include/glm/detail/type_mat4x2.inl
/usr/include/glm/detail/type_mat4x3.hpp
/usr/include/glm/detail/type_mat4x3.inl
/usr/include/glm/detail/type_mat4x4.hpp
/usr/include/glm/detail/type_mat4x4.inl
/usr/include/glm/detail/type_mat4x4_simd.inl
/usr/include/glm/detail/type_vec.hpp
/usr/include/glm/detail/type_vec.inl
/usr/include/glm/detail/type_vec1.hpp
/usr/include/glm/detail/type_vec1.inl
/usr/include/glm/detail/type_vec2.hpp
/usr/include/glm/detail/type_vec2.inl
/usr/include/glm/detail/type_vec3.hpp
/usr/include/glm/detail/type_vec3.inl
/usr/include/glm/detail/type_vec4.hpp
/usr/include/glm/detail/type_vec4.inl
/usr/include/glm/detail/type_vec4_simd.inl
/usr/include/glm/exponential.hpp
/usr/include/glm/ext.hpp
/usr/include/glm/ext/vec1.hpp
/usr/include/glm/ext/vec1.inl
/usr/include/glm/ext/vector_relational.hpp
/usr/include/glm/ext/vector_relational.inl
/usr/include/glm/fwd.hpp
/usr/include/glm/geometric.hpp
/usr/include/glm/glm.hpp
/usr/include/glm/gtc/bitfield.hpp
/usr/include/glm/gtc/bitfield.inl
/usr/include/glm/gtc/color_space.hpp
/usr/include/glm/gtc/color_space.inl
/usr/include/glm/gtc/constants.hpp
/usr/include/glm/gtc/constants.inl
/usr/include/glm/gtc/epsilon.hpp
/usr/include/glm/gtc/epsilon.inl
/usr/include/glm/gtc/integer.hpp
/usr/include/glm/gtc/integer.inl
/usr/include/glm/gtc/matrix_access.hpp
/usr/include/glm/gtc/matrix_access.inl
/usr/include/glm/gtc/matrix_integer.hpp
/usr/include/glm/gtc/matrix_inverse.hpp
/usr/include/glm/gtc/matrix_inverse.inl
/usr/include/glm/gtc/matrix_transform.hpp
/usr/include/glm/gtc/matrix_transform.inl
/usr/include/glm/gtc/noise.hpp
/usr/include/glm/gtc/noise.inl
/usr/include/glm/gtc/packing.hpp
/usr/include/glm/gtc/packing.inl
/usr/include/glm/gtc/quaternion.hpp
/usr/include/glm/gtc/quaternion.inl
/usr/include/glm/gtc/quaternion_simd.inl
/usr/include/glm/gtc/random.hpp
/usr/include/glm/gtc/random.inl
/usr/include/glm/gtc/reciprocal.hpp
/usr/include/glm/gtc/reciprocal.inl
/usr/include/glm/gtc/round.hpp
/usr/include/glm/gtc/round.inl
/usr/include/glm/gtc/type_aligned.hpp
/usr/include/glm/gtc/type_precision.hpp
/usr/include/glm/gtc/type_precision.inl
/usr/include/glm/gtc/type_ptr.hpp
/usr/include/glm/gtc/type_ptr.inl
/usr/include/glm/gtc/ulp.hpp
/usr/include/glm/gtc/ulp.inl
/usr/include/glm/gtc/vec1.hpp
/usr/include/glm/gtc/vec1.inl
/usr/include/glm/gtx/associated_min_max.hpp
/usr/include/glm/gtx/associated_min_max.inl
/usr/include/glm/gtx/bit.hpp
/usr/include/glm/gtx/bit.inl
/usr/include/glm/gtx/closest_point.hpp
/usr/include/glm/gtx/closest_point.inl
/usr/include/glm/gtx/color_encoding.hpp
/usr/include/glm/gtx/color_encoding.inl
/usr/include/glm/gtx/color_space.hpp
/usr/include/glm/gtx/color_space.inl
/usr/include/glm/gtx/color_space_YCoCg.hpp
/usr/include/glm/gtx/color_space_YCoCg.inl
/usr/include/glm/gtx/common.hpp
/usr/include/glm/gtx/common.inl
/usr/include/glm/gtx/compatibility.hpp
/usr/include/glm/gtx/compatibility.inl
/usr/include/glm/gtx/component_wise.hpp
/usr/include/glm/gtx/component_wise.inl
/usr/include/glm/gtx/dual_quaternion.hpp
/usr/include/glm/gtx/dual_quaternion.inl
/usr/include/glm/gtx/easing.hpp
/usr/include/glm/gtx/easing.inl
/usr/include/glm/gtx/euler_angles.hpp
/usr/include/glm/gtx/euler_angles.inl
/usr/include/glm/gtx/extend.hpp
/usr/include/glm/gtx/extend.inl
/usr/include/glm/gtx/extended_min_max.hpp
/usr/include/glm/gtx/extended_min_max.inl
/usr/include/glm/gtx/exterior_product.hpp
/usr/include/glm/gtx/exterior_product.inl
/usr/include/glm/gtx/fast_exponential.hpp
/usr/include/glm/gtx/fast_exponential.inl
/usr/include/glm/gtx/fast_square_root.hpp
/usr/include/glm/gtx/fast_square_root.inl
/usr/include/glm/gtx/fast_trigonometry.hpp
/usr/include/glm/gtx/fast_trigonometry.inl
/usr/include/glm/gtx/float_notmalize.inl
/usr/include/glm/gtx/functions.hpp
/usr/include/glm/gtx/functions.inl
/usr/include/glm/gtx/gradient_paint.hpp
/usr/include/glm/gtx/gradient_paint.inl
/usr/include/glm/gtx/handed_coordinate_space.hpp
/usr/include/glm/gtx/handed_coordinate_space.inl
/usr/include/glm/gtx/hash.hpp
/usr/include/glm/gtx/hash.inl
/usr/include/glm/gtx/integer.hpp
/usr/include/glm/gtx/integer.inl
/usr/include/glm/gtx/intersect.hpp
/usr/include/glm/gtx/intersect.inl
/usr/include/glm/gtx/io.hpp
/usr/include/glm/gtx/io.inl
/usr/include/glm/gtx/log_base.hpp
/usr/include/glm/gtx/log_base.inl
/usr/include/glm/gtx/matrix_cross_product.hpp
/usr/include/glm/gtx/matrix_cross_product.inl
/usr/include/glm/gtx/matrix_decompose.hpp
/usr/include/glm/gtx/matrix_decompose.inl
/usr/include/glm/gtx/matrix_factorisation.hpp
/usr/include/glm/gtx/matrix_factorisation.inl
/usr/include/glm/gtx/matrix_interpolation.hpp
/usr/include/glm/gtx/matrix_interpolation.inl
/usr/include/glm/gtx/matrix_major_storage.hpp
/usr/include/glm/gtx/matrix_major_storage.inl
/usr/include/glm/gtx/matrix_operation.hpp
/usr/include/glm/gtx/matrix_operation.inl
/usr/include/glm/gtx/matrix_query.hpp
/usr/include/glm/gtx/matrix_query.inl
/usr/include/glm/gtx/matrix_transform_2d.hpp
/usr/include/glm/gtx/matrix_transform_2d.inl
/usr/include/glm/gtx/mixed_product.hpp
/usr/include/glm/gtx/mixed_product.inl
/usr/include/glm/gtx/norm.hpp
/usr/include/glm/gtx/norm.inl
/usr/include/glm/gtx/normal.hpp
/usr/include/glm/gtx/normal.inl
/usr/include/glm/gtx/normalize_dot.hpp
/usr/include/glm/gtx/normalize_dot.inl
/usr/include/glm/gtx/number_precision.hpp
/usr/include/glm/gtx/number_precision.inl
/usr/include/glm/gtx/optimum_pow.hpp
/usr/include/glm/gtx/optimum_pow.inl
/usr/include/glm/gtx/orthonormalize.hpp
/usr/include/glm/gtx/orthonormalize.inl
/usr/include/glm/gtx/perpendicular.hpp
/usr/include/glm/gtx/perpendicular.inl
/usr/include/glm/gtx/polar_coordinates.hpp
/usr/include/glm/gtx/polar_coordinates.inl
/usr/include/glm/gtx/projection.hpp
/usr/include/glm/gtx/projection.inl
/usr/include/glm/gtx/quaternion.hpp
/usr/include/glm/gtx/quaternion.inl
/usr/include/glm/gtx/range.hpp
/usr/include/glm/gtx/raw_data.hpp
/usr/include/glm/gtx/raw_data.inl
/usr/include/glm/gtx/rotate_normalized_axis.hpp
/usr/include/glm/gtx/rotate_normalized_axis.inl
/usr/include/glm/gtx/rotate_vector.hpp
/usr/include/glm/gtx/rotate_vector.inl
/usr/include/glm/gtx/scalar_multiplication.hpp
/usr/include/glm/gtx/scalar_relational.hpp
/usr/include/glm/gtx/scalar_relational.inl
/usr/include/glm/gtx/spline.hpp
/usr/include/glm/gtx/spline.inl
/usr/include/glm/gtx/std_based_type.hpp
/usr/include/glm/gtx/std_based_type.inl
/usr/include/glm/gtx/string_cast.hpp
/usr/include/glm/gtx/string_cast.inl
/usr/include/glm/gtx/texture.hpp
/usr/include/glm/gtx/texture.inl
/usr/include/glm/gtx/transform.hpp
/usr/include/glm/gtx/transform.inl
/usr/include/glm/gtx/transform2.hpp
/usr/include/glm/gtx/transform2.inl
/usr/include/glm/gtx/type_aligned.hpp
/usr/include/glm/gtx/type_aligned.inl
/usr/include/glm/gtx/type_trait.hpp
/usr/include/glm/gtx/type_trait.inl
/usr/include/glm/gtx/vec_swizzle.hpp
/usr/include/glm/gtx/vector_angle.hpp
/usr/include/glm/gtx/vector_angle.inl
/usr/include/glm/gtx/vector_query.hpp
/usr/include/glm/gtx/vector_query.inl
/usr/include/glm/gtx/wrap.hpp
/usr/include/glm/gtx/wrap.inl
/usr/include/glm/integer.hpp
/usr/include/glm/mat2x2.hpp
/usr/include/glm/mat2x3.hpp
/usr/include/glm/mat2x4.hpp
/usr/include/glm/mat3x2.hpp
/usr/include/glm/mat3x3.hpp
/usr/include/glm/mat3x4.hpp
/usr/include/glm/mat4x2.hpp
/usr/include/glm/mat4x3.hpp
/usr/include/glm/mat4x4.hpp
/usr/include/glm/matrix.hpp
/usr/include/glm/packing.hpp
/usr/include/glm/simd/common.h
/usr/include/glm/simd/exponential.h
/usr/include/glm/simd/geometric.h
/usr/include/glm/simd/integer.h
/usr/include/glm/simd/matrix.h
/usr/include/glm/simd/packing.h
/usr/include/glm/simd/platform.h
/usr/include/glm/simd/trigonometric.h
/usr/include/glm/simd/vector_relational.h
/usr/include/glm/trigonometric.hpp
/usr/include/glm/vec2.hpp
/usr/include/glm/vec3.hpp
/usr/include/glm/vec4.hpp
/usr/include/glm/vector_relational.hpp
/usr/lib64/cmake/glm/glmConfig.cmake
/usr/lib64/cmake/glm/glmConfigVersion.cmake
/usr/lib64/cmake/glm/glmTargets.cmake
/usr/lib64/pkgconfig/glm.pc
