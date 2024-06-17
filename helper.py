from ultralytics import YOLO
import streamlit as st
import cv2
import PIL
import random
import numpy as np

import settings


def load_model(model_path):
    model = YOLO(model_path)
    return model


def image_config(model, confidence):
    st.sidebar.header("Panoramic Dental X-ray")
    source_radio = st.sidebar.radio("Select Source", settings.SOURCES_LIST)

    source_img = None

    if source_radio == settings.IMAGE:
        source_img = st.sidebar.file_uploader(
            "Choose an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))

        col1, col2 = st.columns(2)

        with col1:
            try:
                if source_img is None:
                    default_image_path = str(settings.DEFAULT_IMAGE)
                    default_image = PIL.Image.open(default_image_path)
                    st.image(default_image, caption="Default Image",
                             use_column_width=True)
                else:
                    uploaded_image = PIL.Image.open(source_img)
                    st.image(uploaded_image, caption="Uploaded Image",
                             use_column_width=True)
            except Exception as ex:
                st.error("Error occurred while opening the image.")
                st.error(ex)

        with col2:
            if source_img is None:
                default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
                default_detected_image = PIL.Image.open(
                    default_detected_image_path)
                st.image(default_detected_image, caption='Detected Image',
                         use_column_width=True)
            else:
                if st.sidebar.button('Detect Objects'):
                    res = model.predict(uploaded_image, conf=confidence)
                    result_image = draw_bounding_boxes(uploaded_image, res, thickness=2)
                    boxes = res[0].boxes
                    #res_plotted = res[0].plot()[:, :, ::-1]
                    st.image(result_image, caption='Detected Image', use_column_width=True)
                    try:
                        with st.expander("Detection Results"):
                            for box in boxes:
                                st.write(box.data)
                    except Exception as ex:
                        st.write("No image is uploaded yet!")

    elif source_radio == settings.EXAMPLE:
        stored_image(confidence, model)

    else:
        st.error("Please select a valid source type!")

    return source_img

def future_development(tittle, figure):
    st.markdown(tittle)
    st.write("We're working on adding a the feature to enhance your experience! Stay tuned for updates.")
    st.write("🚀 Exciting things are coming!")
    st.image(figure, use_column_width=True)


def get_random_color(seed):
    random.seed()
    return tuple(random.randint(0, 255) for _ in range(3))

def draw_bounding_boxes(image, results, thickness=2):
    image = np.array(image)
    image = image[:, :, ::-1].copy()  # Convert RGB to BGR

    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        confidence = box.conf[0]
        class_id = int(box.cls[0])
        label = f"{class_id}"
        
        color = get_random_color(class_id)
        cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)

        (text_width, text_height), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.9, 2)
        
        cv2.rectangle(image, (x1, y1 - text_height - 10), (x1 + text_width, y1), color, -1)
        cv2.putText(image, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    image = image[:, :, ::-1]
    return image

def stored_image(confidence, model):
    source_img = st.sidebar.selectbox(
        "Choose an image...", list(settings.IMAGES_DICT.keys()))

    default_image = PIL.Image.open(settings.IMAGES_DICT[source_img])
    st.image(default_image, caption="Selected Image", use_column_width=True)

    if st.sidebar.button('Detect Teeth'):
        st.write("Teeth detection : ")
        image = PIL.Image.open(settings.IMAGES_DICT[source_img])
        res = model.predict(image, conf=confidence)

        #boxes = res[0].boxes
        #res_plotted = res[0].plot()[:, :, ::-1]
        
        result_image = draw_bounding_boxes(image, res, thickness=2)
        
        st.image(result_image, caption='Detected Image', use_column_width=True)

        #teeth_detection_result = detect_teeth(image, model)


