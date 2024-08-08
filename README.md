# Conversor de email webpay transbank a imagen

Lo archivos presentes en el repositorio tienen el propósito de leer los archivos .eml en alguna carpeta seleccionada, cambiarles el nombre con el formato RUT Nombre.eml; 
crear un csv con los parámetros dentro del archivo y hacer una foto de ese.

## Modo de uso 

### Cambiar nombres y crear csv (*nombre_y_csv.py*)

Para cambiar los nombres de los archivos .eml y crear un csv con los parámetros de este, se debe correr *nombre_y_csv.py*.
Este pedirá el nombre de la carpeta donde se encuentren los archivos .eml, lo cual una vez proporcionado comenzará a cambiar los nombres y 
creará el csv en la ruta inicial.

![image](https://github.com/user-attachments/assets/86bdb4da-e776-4398-a8ca-7e1a006951bd)

### Crear imágenes (*html_to_image.py*)

Para crear las imágenes a partir de los .eml, se debe correr el script *html_to_image.py*, este pedirá la carpeta en donde se encuentran los archivos .eml
y una segunda carpeta en la que se quieran poner las imágenes, se debe tener en cuenta que para esta última, si no se encuentra creada la carpeta, se creará una con el nombre escogido en el input.

