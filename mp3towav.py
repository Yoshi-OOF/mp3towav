from pydub import AudioSegment
import os

def convert_mp3_to_wav():
    source_folder = input("Entrez le chemin du dossier source : ")
    target_folder = input("Entrez le chemin du dossier cible : ")

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for filename in os.listdir(source_folder):
        if filename.endswith('.mp3'):
            mp3_path = os.path.join(source_folder, filename)
            wav_filename = filename.replace('.mp3', '.wav')
            wav_path = os.path.join(target_folder, wav_filename)

            audio = AudioSegment.from_mp3(mp3_path)
            audio.export(wav_path, format="wav")

            print(f"Converti {filename} en WAV.")

convert_mp3_to_wav()
