from IPython import get_ipython
from IPython.display import display
# %%
pip install mammoth

import os
import mammoth
import argparse
import codecs
from glob import glob


def convert_doc_to_md(input_file, output_file):
    """
    Convierte un archivo .doc o .docx a .md con codificación UTF-8 sin BOM

    Args:
        input_file: Ruta al archivo .doc/.docx a convertir
        output_file: Ruta donde guardar el archivo .md resultante
    """
    try:
        with open(input_file, "rb") as docx_file:
            # Convertir DOCX a HTML
            result = mammoth.convert_to_markdown(docx_file)
            markdown = result.value

            # Guardar como UTF-8 sin BOM
            with codecs.open(output_file, "w", encoding="utf-8") as md_file:
                md_file.write(markdown)

            # Mostrar mensajes de advertencia si los hay
            if result.messages:
                print(f"Advertencias para {input_file}:")
                for message in result.messages:
                    print(f"  • {message}")

            print(f"✅ Convertido: {input_file} → {output_file}")
            return True
    except Exception as e:
        print(f"❌ Error al convertir {input_file}: {str(e)}")
        return False


def process_directory(input_dir, output_dir, recursive=False):
    """
    Procesa todos los archivos .doc/.docx en un directorio

    Args:
        input_dir: Directorio de entrada con archivos .doc/.docx
        output_dir: Directorio donde guardar los archivos .md
        recursive: Si se deben buscar archivos en subdirectorios
    """
    # Asegurar que el directorio de salida exista
    os.makedirs(output_dir, exist_ok=True)

    # Patrón de búsqueda
    pattern = os.path.join(input_dir, "**" if recursive else "", "*.doc*")

    # Obtener lista de archivos
    files = glob(pattern, recursive=recursive)

    if not files:
        print(f"No se encontraron archivos .doc/.docx en '{input_dir}'")
        return

    print(f"Encontrados {len(files)} archivos .doc/.docx para convertir")

    # Contador de éxitos
    success_count = 0

    # Procesar cada archivo
    for doc_file in files:
        # Obtener ruta relativa del archivo de entrada
        rel_path = os.path.relpath(doc_file, input_dir)

        # Construir ruta de salida cambiando la extensión a .md
        base_name = os.path.splitext(rel_path)[0]
        output_file = os.path.join(output_dir, f"{base_name}.md")

        # Asegurar que exista el directorio de salida (para archivos en subdirectorios)
        os.makedirs(os.path.dirname(output_file) or '.', exist_ok=True)

        # Convertir archivo
        if convert_doc_to_md(doc_file, output_file):
            success_count += 1

    # Resumen
    print(f"\nConversión completada: {success_count} de {len(files)} archivos convertidos correctamente")


def main(args_list=None): # Added args_list parameter
    parser = argparse.ArgumentParser(description='Convertir archivos .doc/.docx a .md (UTF-8 sin BOM)')
    parser.add_argument('input', help='Archivo o directorio de entrada')
    parser.add_argument('-o', '--output', help='Archivo o directorio de salida (por defecto: igual que entrada con extensión .md)')
    parser.add_argument('-r', '--recursive', action='store_true', help='Buscar archivos recursivamente en subdirectorios')

    # Pass the args_list to parse_args
    args = parser.parse_args(args_list)

    # Comprobar si la entrada es un archivo o directorio
    if os.path.isfile(args.input):
        # Es un archivo único
        if not args.output:
            # Si no se especifica salida, usar el mismo nombre con extensión .md
            base_name = os.path.splitext(args.input)[0]
            output_file = f"{base_name}.md"
        else:
            output_file = args.output

        # Asegurar que exista el directorio de salida
        os.makedirs(os.path.dirname(output_file) or '.', exist_ok=True)

        # Convertir archivo
        if convert_doc_to_md(args.input, output_file):
            print("\nConversión completada correctamente")
        else:
            print("\nLa conversión falló")

    elif os.path.isdir(args.input):
        # Es un directorio
        output_dir = args.output if args.output else args.input
        process_directory(args.input, output_dir, args.recursive)

    else:
        print(f"Error: La ruta de entrada '{args.input}' no existe")


if __name__ == "__main__":
    print("Conversor de DOC a MD (UTF-8 sin BOM)")
    print("=====================================")
    # Simulate command-line arguments by passing a list
    # Replace 'your_input_directory' with the actual path you want to process
    # Example for a directory: main(['your_input_directory', '-r'])
from IPython import get_ipython
from IPython.display import display
# %%
get_ipython().run_line_magic('pip', 'install mammoth')

import os
import mammoth
import argparse
import codecs
from glob import glob


def convert_doc_to_md(input_file, output_file):
    """
    Convierte un archivo .doc o .docx a .md con codificación UTF-8 sin BOM

    Args:
        input_file: Ruta al archivo .doc/.docx a convertir
        output_file: Ruta donde guardar el archivo .md resultante
    """
    try:
        with open(input_file, "rb") as docx_file:
            # Convertir DOCX a HTML
            result = mammoth.convert_to_markdown(docx_file)
            markdown = result.value

            # Guardar como UTF-8 sin BOM
            with codecs.open(output_file, "w", encoding="utf-8") as md_file:
                md_file.write(markdown)

            # Mostrar mensajes de advertencia si los hay
            if result.messages:
                print(f"Advertencias para {input_file}:")
                for message in result.messages:
                    print(f"  • {message}")

            print(f"✅ Convertido: {input_file} → {output_file}")
            return True
    except Exception as e:
        print(f"❌ Error al convertir {input_file}: {str(e)}")
        return False


def process_directory(input_dir, output_dir, recursive=False):
    """
    Procesa todos los archivos .doc/.docx en un directorio

    Args:
        input_dir: Directorio de entrada con archivos .doc/.docx
        output_dir: Directorio donde guardar los archivos .md
        recursive: Si se deben buscar archivos en subdirectorios
    """
    # Asegurar que el directorio de salida exista
    os.makedirs(output_dir, exist_ok=True)

    # Patrón de búsqueda
    pattern = os.path.join(input_dir, "**" if recursive else "", "*.doc*")

    # Obtener lista de archivos
    files = glob(pattern, recursive=recursive)

    if not files:
        print(f"No se encontraron archivos .doc/.docx en '{input_dir}'")
        return

    print(f"Encontrados {len(files)} archivos .doc/.docx para convertir")

    # Contador de éxitos
    success_count = 0

    # Procesar cada archivo
    for doc_file in files:
        # Obtener ruta relativa del archivo de entrada
        rel_path = os.path.relpath(doc_file, input_dir)

        # Construir ruta de salida cambiando la extensión a .md
        base_name = os.path.splitext(rel_path)[0]
        output_file = os.path.join(output_dir, f"{base_name}.md")

        # Asegurar que exista el directorio de salida (para archivos en subdirectorios)
        os.makedirs(os.path.dirname(output_file) or '.', exist_ok=True)

        # Convertir archivo
        if convert_doc_to_md(doc_file, output_file):
            success_count += 1

    # Resumen
    print(f"\nConversión completada: {success_count} de {len(files)} archivos convertidos correctamente")


def main(args_list=None): # Added args_list parameter
    parser = argparse.ArgumentParser(description='Convertir archivos .doc/.docx a .md (UTF-8 sin BOM)')
    parser.add_argument('input', help='Archivo o directorio de entrada')
    parser.add_argument('-o', '--output', help='Archivo o directorio de salida (por defecto: igual que entrada con extensión .md)')
    parser.add_argument('-r', '--recursive', action='store_true', help='Buscar archivos recursivamente en subdirectorios')

    # Pass the args_list to parse_args
    args = parser.parse_args(args_list)

    # Comprobar si la entrada es un archivo o directorio
    if os.path.isfile(args.input):
        # Es un archivo único
        if not args.output:
            # Si no se especifica salida, usar el mismo nombre con extensión .md
            base_name = os.path.splitext(args.input)[0]
            output_file = f"{base_name}.md"
        else:
            output_file = args.output

        # Asegurar que exista el directorio de salida
        os.makedirs(os.path.dirname(output_file) or '.', exist_ok=True)

        # Convertir archivo
        if convert_doc_to_md(args.input, output_file):
            print("\nConversión completada correctamente")
        else:
            print("\nLa conversión falló")

    elif os.path.isdir(args.input):
        # Es un directorio
        output_dir = args.output if args.output else args.input
        process_directory(args.input, output_dir, args.recursive)

    else:
        print(f"Error: La ruta de entrada '{args.input}' no existe")


if __name__ == "__main__":
    print("Conversor de DOC a MD (UTF-8 sin BOM)")
    print("=====================================")
    # Simulate command-line arguments by passing a list
    # Replace 'your_input_directory' with the actual path you want to process
    # Example for a directory: main(['your_input_directory', '-r'])
from IPython import get_ipython
from IPython.display import display
# %%
get_ipython().run_line_magic('pip', 'install mammoth')

import os
import mammoth
import argparse
import codecs
from glob import glob


def convert_doc_to_md(input_file, output_file):
    """
    Convierte un archivo .doc o .docx a .md con codificación UTF-8 sin BOM

    Args:
        input_file: Ruta al archivo .doc/.docx a convertir
        output_file: Ruta donde guardar el archivo .md resultante
    """
    try:
        with open(input_file, "rb") as docx_file:
            # Convertir DOCX a HTML
            result = mammoth.convert_to_markdown(docx_file)
            markdown = result.value

            # Guardar como UTF-8 sin BOM
            with codecs.open(output_file, "w", encoding="utf-8") as md_file:
                md_file.write(markdown)

            # Mostrar mensajes de advertencia si los hay
            if result.messages:
                print(f"Advertencias para {input_file}:")
                for message in result.messages:
                    print(f"  • {message}")

            print(f"✅ Convertido: {input_file} → {output_file}")
            return True
    except Exception as e:
        print(f"❌ Error al convertir {input_file}: {str(e)}")
        return False


def process_directory(input_dir, output_dir, recursive=False):
    """
    Procesa todos los archivos .doc/.docx en un directorio

    Args:
        input_dir: Directorio de entrada con archivos .doc/.docx
        output_dir: Directorio donde guardar los archivos .md
        recursive: Si se deben buscar archivos en subdirectorios
    """
    # Asegurar que el directorio de salida exista
    os.makedirs(output_dir, exist_ok=True)

    # Patrón de búsqueda
    pattern = os.path.join(input_dir, "**" if recursive else "", "*.doc*")

    # Obtener lista de archivos
    files = glob(pattern, recursive=recursive)

    if not files:
        print(f"No se encontraron archivos .doc/.docx en '{input_dir}'")
        return

    print(f"Encontrados {len(files)} archivos .doc/.docx para convertir")

    # Contador de éxitos
    success_count = 0

    # Procesar cada archivo
    for doc_file in files:
        # Obtener ruta relativa del archivo de entrada
        rel_path = os.path.relpath(doc_file, input_dir)

        # Construir ruta de salida cambiando la extensión a .md
        base_name = os.path.splitext(rel_path)[0]
        output_file = os.path.join(output_dir, f"{base_name}.md")

        # Asegurar que exista el directorio de salida (para archivos en subdirectorios)
        os.makedirs(os.path.dirname(output_file) or '.', exist_ok=True)

        # Convertir archivo
        if convert_doc_to_md(doc_file, output_file):
            success_count += 1

    # Resumen
    print(f"\nConversión completada: {success_count} de {len(files)} archivos convertidos correctamente")


def main(args_list=None): # Added args_list parameter
    parser = argparse.ArgumentParser(description='Convertir archivos .doc/.docx a .md (UTF-8 sin BOM)')
    parser.add_argument('input', help='Archivo o directorio de entrada')
    parser.add_argument('-o', '--output', help='Archivo o directorio de salida (por defecto: igual que entrada con extensión .md)')
    parser.add_argument('-r', '--recursive', action='store_true', help='Buscar archivos recursivamente en subdirectorios')

    # Pass the args_list to parse_args
    args = parser.parse_args(args_list)

    # Comprobar si la entrada es un archivo o directorio
    if os.path.isfile(args.input):
        # Es un archivo único
        if not args.output:
            # Si no se especifica salida, usar el mismo nombre con extensión .md
            base_name = os.path.splitext(args.input)[0]
            output_file = f"{base_name}.md"
        else:
            output_file = args.output

        # Asegurar que exista el directorio de salida
        os.makedirs(os.path.dirname(output_file) or '.', exist_ok=True)

        # Convertir archivo
        if convert_doc_to_md(args.input, output_file):
            print("\nConversión completada correctamente")
        else:
            print("\nLa conversión falló")

    elif os.path.isdir(args.input):
        # Es un directorio
        output_dir = args.output if args.output else args.input
        process_directory(args.input, output_dir, args.recursive)

    else:
        print(f"Error: La ruta de entrada '{args.input}' no existe")


if __name__ == "__main__":
    print("Conversor de DOC a MD (UTF-8 sin BOM)")
    print("=====================================")
    # Simulate command-line arguments by passing a list
    # Replace 'your_input_directory' with the actual path you want to process
    # Example for a directory: main(['your_input_directory', '-r'])
    # Example for a single file: main(['your_input_file.docx', '-o', 'output.md'])
    # For now, we'll use a placeholder. You need to uncomment and modify the line below.
    main(['objects\transcripciones']) # <-- Uncomment and modify this line
    print("To run this code in the notebook, uncomment and modify the 'main' call below this section.")
    print("Example: main(['./path/to/your/docs_folder', '-r', '-o', './output_markdown'])")
