import cv2
import numpy as np
import PIL.Image as Image

def guided_color_refine(enhanced_img):
    """
    Safe, drop-in replacement for guided color refinement.
    - Accepts: numpy, PIL, torch, tf tensors
    - Never crashes on cvtColor
    - Ensures uint8 BGR image
    - Ensures matching channel sizes
    - Uses bilateral filtering for edge-preserving refinement
    """

    # ---------------------------
    # Convert ANY input to NumPy
    # ---------------------------
    if enhanced_img is None:
        raise ValueError("guided_color_refine() received None as input.")

    # TensorFlow tensor
    if hasattr(enhanced_img, "numpy"):
        enhanced_img = enhanced_img.numpy()

    # PyTorch tensor
    if hasattr(enhanced_img, "detach"):
        enhanced_img = enhanced_img.detach().cpu().numpy()

    # PIL image
    if not isinstance(enhanced_img, np.ndarray):
        try:
            enhanced_img = np.array(enhanced_img)
        except:
            raise TypeError(f"Unsupported image type: {type(enhanced_img)}")

    # Ensure uint8 3-channel BGR
    if enhanced_img.dtype != np.uint8:
        enhanced_img = enhanced_img.astype(np.uint8)

    if len(enhanced_img.shape) != 3 or enhanced_img.shape[2] != 3:
        raise ValueError("guided_color_refine() expects a BGR image (H,W,3).")

    # ---------------------------
    # Convert to LAB
    # ---------------------------
    try:
        lab = cv2.cvtColor(enhanced_img, cv2.COLOR_BGR2LAB)
    except Exception as e:
        raise RuntimeError(f"cvtColor failed: {e}")

    L, A, B = cv2.split(lab)

    # ---------------------------
    # Bilateral refinement (safer than ximgproc)
    # ---------------------------
    A_ref = cv2.bilateralFilter(A, 9, 75, 75)
    B_ref = cv2.bilateralFilter(B, 9, 75, 75)

    # Ensure matching shapes
    h, w = L.shape
    A_ref = cv2.resize(A_ref, (w, h))
    B_ref = cv2.resize(B_ref, (w, h))

    # ---------------------------
    # Merge back to LAB
    # ---------------------------
    lab_ref = cv2.merge([L, A_ref, B_ref])

    # ---------------------------
    # Convert back to BGR
    # ---------------------------
    refined_bgr = cv2.cvtColor(lab_ref, cv2.COLOR_LAB2BGR)

    pil_img = Image.fromarray(refined_bgr)
    
    return pil_img
