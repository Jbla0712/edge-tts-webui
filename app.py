import gradio as gr
import edge_tts
import asyncio

# Fonction pour convertir le texte en audio
async def text_to_speech(text, voice='fr-FR-HenriNeural'):
    communicate = edge_tts.Communicate(text, voice)
    audio = await communicate.save("output.mp3")  # Enregistrer directement dans un fichier
    return "output.mp3"  # Retourner le chemin du fichier audio généré

# Fonction pour créer l'interface Gradio
def create_interface():
    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column():
                text_input = gr.Textbox(label="Entrez le texte")
                voice_input = gr.Dropdown(
                    label="Choisissez la voix",
                    choices=[
                        'fr-BE-GerardNeural', 'fr-CA-AntoineNeural', 'fr-CA-JeanNeural',
                        'fr-CA-SylvieNeural', 'fr-CA-ThierryNeural', 'fr-CH-ArianeNeural',
                        'fr-CH-FabriceNeural', 'fr-FR-DeniseNeural', 'fr-FR-EloiseNeural',
                        'fr-FR-HenriNeural', 'fr-FR-RemyMultilingualNeural', 'fr-FR-VivienneMultilingualNeural'
                    ],
                    value='fr-FR-HenriNeural'  # Voix par défaut
                )
                output_audio = gr.Audio(label="Audio généré")
                submit_button = gr.Button("Générer")
                submit_button.click(
                    fn=lambda text, voice: asyncio.run(text_to_speech(text, voice)),
                    inputs=[text_input, voice_input],
                    outputs=[output_audio]
                )
    return demo

if __name__ == "__main__":
    demo = create_interface()
    demo.launch()
