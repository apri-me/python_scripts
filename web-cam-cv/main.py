import cv2
import numpy as np
import sys

def verify_alpha_channel(frame):
    try:
        frame.shape[3]
    except IndexError:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    return frame

def apply_invert(frame):
    return cv2.bitwise_not(frame)

def apply_color_overlay(frame, blue, green, red, intensity=.4):
    frame = verify_alpha_channel(frame)
    frame_h, frame_w, frame_c = frame.shape
    sepia_bgra = (blue, green, red, 1)
    overlay = np.full((frame_h, frame_w, 4), sepia_bgra, dtype='uint8')
    cv2.addWeighted(overlay, intensity, frame, 1, 0, frame)
    return frame

def alpha_blend(frame_1, frame_2, mask):
    alpha = mask/255.0 
    blended = cv2.convertScaleAbs(frame_1*(1-alpha) + frame_2*alpha)
    return blended

def apply_circle_focus_blur(frame, intensity=.2):
    frame = verify_alpha_channel(frame)
    frame_h, frame_w, frame_c = frame.shape
    x = int(frame_w/2)
    y = int(frame_h/2)
    radius = int(y/2)
    center = (x, y)
    mask = np.zeros((frame_h, frame_w, 4), dtype='uint8')
    cv2.circle(mask, center, radius, (255, 255, 255), -1, cv2.LINE_AA)
    mask = cv2.GaussianBlur(mask, (21,21), 11)
    blured = cv2.GaussianBlur(frame, (21,21), 11)
    blended = alpha_blend(frame, blured, 255 - mask)
    frame = cv2.cvtColor(blended, cv2.COLOR_BGRA2BGR)
    return frame

def apply_hue_saturation(frame, alpha=6, beta=6):
    frame = verify_alpha_channel(frame)
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_image)
    s.fill(199)
    v.fill(255)
    hsv_image = cv2.merge([h, s, v])

    out = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    frame = verify_alpha_channel(frame)
    out = verify_alpha_channel(out)
    cv2.addWeighted(out, 0.25, frame, 1.0, .23, frame)
    return frame

def apply_treshold(frame, trs_value=80):
    frame = verify_alpha_channel(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, trs_value, 255, cv2.THRESH_BINARY)
    return mask

# def apply_portrait_mode(frame):
#     mask = apply_treshold(frame)
#     mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGRA)
#     blured = cv2.GaussianBlur(frame, (21,21), 11)
#     blended = alpha_blend(frame, blured, mask)
#     frame = cv2.cvtColor(blended, cv2.COLOR_BGRA2BGR)
#     return frame

def toggle_effect(ef_op, effect):
    if effect in ef_op:
        ef_op.remove(effect)
    else:
        ef_op.append(effect)

effect_funcs = {
    'INV': apply_invert,
    'FOC': apply_circle_focus_blur,
    'HUE': apply_hue_saturation,
    'TRS': apply_treshold,
    # 'POR': portrait_mode,
}

# BGR
color_channels = {
    'SEP': (20, 66, 112),
    'RED': (0, 0, 255),
    'GRN': (0, 255, 0),
    'BLU': (255, 0, 0),
}

vid = cv2.VideoCapture(0)

effect_options = []
color_overlay_options = []
wk = -1

while 1:
    ret, frame = vid.read()
    if ret:
        ### NOTE: Size, Crop and Rotation
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame,(400,650),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        frame = frame[:400, :600]
        ###
        ### NOTE: Effects
        cv2.normalize(frame, frame, -50, 280, cv2.NORM_MINMAX)
        for ef in effect_options: 
            frame = effect_funcs[ef](frame)
        for co in color_overlay_options: 
            frame = apply_color_overlay(frame, *color_channels[co])
        ###
        last_key = wk
        wk = cv2.waitKey(1) & 0xFF
        if wk == ord('q'):
            break
        if wk == ord('i'):
            toggle_effect(effect_options, 'INV')
        if wk == ord('f'):
            toggle_effect(effect_options, 'FOC')
        if wk == ord('h'):
            toggle_effect(effect_options, 'HUE')
        if wk == ord('t'):
            toggle_effect(effect_options, 'TRS')
        # if wk == ord('p'):
        #     toggle_effect(effect_options, 'POR')
        
        if wk == ord('s'):
            toggle_effect(color_overlay_options, 'SEP')
        if wk == ord('r'):
            toggle_effect(color_overlay_options, 'RED')
        if wk == ord('g'):
            toggle_effect(color_overlay_options, 'GRN')
        if wk == ord('b'):
            toggle_effect(color_overlay_options, 'BLU')

        cv2.imshow('camera', frame)

vid.release()