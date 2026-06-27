[app]
title = ChromaticGenMobile
package.name = chromaticgenmobile
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Dependencias necesarias
requirements = python3,kivy,praat-parselmouth,requests,setuptools

orientation = portrait
fullscreen = 0

# Permisos críticos para leer los archivos de audio en el móvil
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Configuración de arquitectura y APIs
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = True

# Formatos de salida
android.release_artifact = aab
android.debug_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
