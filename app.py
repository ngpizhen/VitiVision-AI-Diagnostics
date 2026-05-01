import gradio as gr
import numpy as np
from PIL import Image
import tensorflow as tf

CLASS_NAMES = ['Grape Black Rot', 'Grape Esca (Black Measles)', 'Healthy']

def predict_disease(image):
    if image is None: return None
    image = image.resize((224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(image)
    img_array = np.expand_dims(img_array, axis=0) / 255.0 
    predictions = model_transfer.predict(img_array)[0]
    return {CLASS_NAMES[i]: float(predictions[i]) for i in range(len(CLASS_NAMES))}

theme = gr.themes.Soft(
    primary_hue="purple",    
    secondary_hue="green",   
).set(
    button_primary_background_fill="*primary_600",
    button_primary_background_fill_hover="*primary_700",
)

with gr.Blocks(theme=theme) as interface:
    gr.Markdown(
        """
        # 🍇 VitiVision: AI-Powered Viticulture Diagnostics
        ### **Protecting Vineyards through Transfer Learning (MobileNetV2)**
        *Upload a grape leaf photo to receive an instant health assessment with **96.33% accuracy**.*
        """
    )
    
    with gr.Row():
        with gr.Column(scale=1):
            input_img = gr.Image(
                type="pil", 
                label="Step 1: Upload Grape Leaf Image",
                elem_id="image_upload"
            )
            btn = gr.Button("🔍 Run Diagnostic", variant="primary")
            
        with gr.Column(scale=1):
            output_label = gr.Label(
                num_top_classes=3, 
                label="Step 2: Diagnostic Results"
            )
    btn.click(fn=predict_disease, inputs=input_img, outputs=output_label)

    gr.Markdown(
        """
        ---
        **Technical Highlights:**
        - **Model:** Fine-tuned MobileNetV2
        - **Precision:** 100% precision on 'Healthy' class detection
        - **Inference Speed:** Real-time analysis[cite: 2]
        """
    )

interface.launch(share=True)
