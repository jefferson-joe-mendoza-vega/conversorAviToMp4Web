# Video Converter para Web

## Descripción
Video Converter para Web es una aplicación de escritorio que permite convertir fácilmente archivos de video (como AVI, MKV, MOV, etc.) a formatos compatibles con navegadores web (MP4 con H.264 o WebM con VP9). Esta herramienta está diseñada para ser simple de usar y no requiere conocimientos técnicos.

## Características principales
- Interfaz gráfica intuitiva desarrollada con Tkinter
- Conversión de múltiples formatos de video a MP4/WebM optimizados para web
- Opciones de selección de formato (MP4/WebM) y códec (H.264/VP9)
- Barra de progreso para seguir el avance de la conversión
- Procesamiento en segundo plano que no bloquea la interfaz

## Requisitos del sistema
- Sistema operativo: Windows, macOS o Linux
- No requiere instalación de software adicional (el ejecutable incluye todas las dependencias)
- Espacio en disco: ~50 MB para la aplicación, más espacio adicional para los videos procesados

## Cómo utilizar
1. Ejecute la aplicación haciendo doble clic en el icono del programa
2. Haga clic en "Seleccionar Video" para elegir el archivo que desea convertir
3. (Opcional) Haga clic en "Directorio de salida" para elegir dónde guardar el archivo convertido
4. Seleccione el formato deseado (MP4 o WebM) y el códec
5. Haga clic en "Convertir para Web"
6. Espere a que finalice la conversión
7. El archivo convertido estará disponible en la ubicación seleccionada

## Formatos recomendados
- **MP4 con H.264**: Máxima compatibilidad con todos los navegadores modernos
- **WebM con VP9**: Mejor compresión, ideal para sitios que soportan este formato

## Notas técnicas
- La aplicación utiliza OpenCV para procesar los videos
- Los archivos resultantes están optimizados para reproducción en navegadores web
- El ejecutable fue creado con PyInstaller para facilitar su distribución

## Limitaciones
- Dependiendo de la complejidad del video, el proceso puede tomar varios minutos
- Posible pérdida de calidad en la conversión dependiendo del formato original
- La aplicación no modifica metadatos ni preserva capítulos
- No se recomienda para conversiones por lotes de gran volumen

## Créditos
Desarrollado como una herramienta de utilidad para simplificar la conversión de videos para uso web.

Fecha de creación: Agosto 2023
