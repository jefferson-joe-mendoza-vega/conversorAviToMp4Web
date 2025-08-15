import os
import cv2
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
from tkinter import StringVar, OptionMenu

class VideoConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Video para Web")
        self.root.geometry("550x380")
        self.root.resizable(False, False)
        
        self.input_file = ""
        self.output_directory = ""
        self.format_option = StringVar(value="mp4")
        self.codec_option = StringVar(value="H264")
        
        # Estilo
        self.root.configure(bg="#f0f0f0")
        
        # Crear interfaz
        self.create_widgets()
    
    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)
        
        # Título
        tk.Label(main_frame, text="Convertidor de Video para Web", font=("Arial", 16, "bold"), 
                 bg="#f0f0f0", fg="#333333").pack(pady=(0, 15))
        
        # Frame para los botones de selección
        select_frame = tk.Frame(main_frame, bg="#f0f0f0")
        select_frame.pack(fill="x", pady=5)
        
        # Botón para seleccionar archivo de video
        self.input_label = tk.Label(select_frame, text="Ningún archivo seleccionado", 
                                   bg="#f0f0f0", fg="#555555", width=40)
        self.input_label.pack(side=tk.LEFT, padx=(0, 10))
        
        select_button = tk.Button(select_frame, text="Seleccionar Video", command=self.select_file,
                                 bg="#4CAF50", fg="white", relief=tk.FLAT, padx=10)
        select_button.pack(side=tk.RIGHT)
        
        # Frame para el directorio de salida
        output_frame = tk.Frame(main_frame, bg="#f0f0f0")
        output_frame.pack(fill="x", pady=5)
        
        # Botón para seleccionar directorio de salida
        self.output_label = tk.Label(output_frame, text="Directorio de salida predeterminado", 
                                    bg="#f0f0f0", fg="#555555", width=40)
        self.output_label.pack(side=tk.LEFT, padx=(0, 10))
        
        output_button = tk.Button(output_frame, text="Directorio de salida", command=self.select_output_directory,
                                 bg="#2196F3", fg="white", relief=tk.FLAT, padx=10)
        output_button.pack(side=tk.RIGHT)
        
        # Frame para opciones de formato
        options_frame = tk.Frame(main_frame, bg="#f0f0f0")
        options_frame.pack(fill="x", pady=10)
        
        # Opciones de formato
        tk.Label(options_frame, text="Formato:", bg="#f0f0f0", fg="#333333").pack(side=tk.LEFT, padx=(0, 5))
        format_menu = OptionMenu(options_frame, self.format_option, "mp4", "webm")
        format_menu.config(width=5)
        format_menu.pack(side=tk.LEFT, padx=(0, 20))
        
        # Opciones de códec
        tk.Label(options_frame, text="Códec:", bg="#f0f0f0", fg="#333333").pack(side=tk.LEFT, padx=(0, 5))
        codec_menu = OptionMenu(options_frame, self.codec_option, "H264", "VP9")
        codec_menu.config(width=5)
        codec_menu.pack(side=tk.LEFT)
        
        # Barra de progreso
        self.progress = ttk.Progressbar(main_frame, orient="horizontal", length=510, mode="determinate")
        self.progress.pack(pady=15)
        
        # Etiqueta de estado
        self.status_label = tk.Label(main_frame, text="Listo para convertir", 
                                    bg="#f0f0f0", fg="#555555")
        self.status_label.pack(pady=(0, 15))
        
        # Botón para convertir
        self.convert_button = tk.Button(main_frame, text="Convertir para Web", command=self.start_conversion,
                                      bg="#FF5722", fg="white", relief=tk.FLAT, 
                                      padx=20, pady=10, font=("Arial", 12))
        self.convert_button.pack()
        
        # Nota sobre el audio
        note_label = tk.Label(main_frame, text="Nota: Este convertidor puede no preservar el audio original", 
                             bg="#f0f0f0", fg="#888888", font=("Arial", 8, "italic"))
        note_label.pack(pady=(10, 0))
    
    def select_file(self):
        self.input_file = filedialog.askopenfilename(
            title="Seleccione un archivo de video",
            filetypes=[
                ("Archivos de video", "*.avi *.mp4 *.mkv *.mov *.wmv"),
                ("Todos los archivos", "*.*")
            ]
        )
        if self.input_file:
            file_name = os.path.basename(self.input_file)
            self.input_label.config(text=file_name)
    
    def select_output_directory(self):
        self.output_directory = filedialog.askdirectory(title="Seleccione directorio de salida")
        if self.output_directory:
            dir_name = os.path.basename(self.output_directory)
            self.output_label.config(text=dir_name)
    
    def start_conversion(self):
        if not self.input_file:
            messagebox.showerror("Error", "Debe seleccionar un archivo de video para convertir.")
            return
        
        # Si no se seleccionó un directorio de salida, usar el mismo del archivo de entrada
        if not self.output_directory:
            self.output_directory = os.path.dirname(self.input_file)
            self.output_label.config(text=os.path.basename(self.output_directory))
        
        # Crear el nombre del archivo de salida
        input_filename = os.path.basename(self.input_file)
        output_filename = os.path.splitext(input_filename)[0] + "." + self.format_option.get()
        output_path = os.path.join(self.output_directory, output_filename)
        
        # Deshabilitar el botón durante la conversión
        self.convert_button.config(state=tk.DISABLED)
        
        # Iniciar la conversión en un hilo separado
        thread = threading.Thread(target=self.convert_video, args=(output_path,))
        thread.daemon = True
        thread.start()
    
    def convert_video(self, output_path):
        try:
            self.status_label.config(text="Abriendo archivo de video...")
            self.progress["value"] = 10
            self.root.update_idletasks()
            
            # Abrir el archivo de video
            cap = cv2.VideoCapture(self.input_file)
            if not cap.isOpened():
                raise Exception("No se pudo abrir el archivo de video")
            
            # Obtener información del video
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            self.status_label.config(text="Preparando archivo de salida...")
            self.progress["value"] = 20
            self.root.update_idletasks()
            
            # Define el codec según la selección del usuario
            if self.format_option.get() == "mp4":
                if self.codec_option.get() == "H264":
                    fourcc = cv2.VideoWriter_fourcc(*'avc1')  # H.264 codec para web
                else:
                    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec alternativo
            else:  # webm
                if self.codec_option.get() == "VP9":
                    fourcc = cv2.VideoWriter_fourcc(*'VP90')  # VP9 codec para WebM
                else:
                    fourcc = cv2.VideoWriter_fourcc(*'VP80')  # VP8 codec
            
            # Crear el objeto VideoWriter
            out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
            
            # Procesar el video cuadro por cuadro
            self.status_label.config(text="Convirtiendo video...")
            
            frame_count = 0
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                # Escribir el cuadro en el archivo de salida
                out.write(frame)
                
                # Actualizar progreso
                frame_count += 1
                progress_percent = int((frame_count / total_frames) * 80) + 20  # 20-100%
                self.progress["value"] = min(progress_percent, 100)
                
                # Actualizar UI cada 30 cuadros para no ralentizar el proceso
                if frame_count % 30 == 0:
                    self.status_label.config(text=f"Convirtiendo... {frame_count}/{total_frames} cuadros")
                    self.root.update_idletasks()
            
            # Liberar recursos
            cap.release()
            out.release()
            
            self.progress["value"] = 100
            self.status_label.config(text=f"Conversión completa. Guardado en: {output_path}")
            messagebox.showinfo("Éxito", f"La conversión ha finalizado correctamente.\n\nArchivo guardado en:\n{output_path}")
            
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")
            messagebox.showerror("Error", f"Ocurrió un error durante la conversión:\n{str(e)}")
        
        finally:
            # Restaurar la interfaz
            self.convert_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoConverter(root)
    root.mainloop()
