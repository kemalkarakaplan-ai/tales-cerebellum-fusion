import numpy as np

class TalesCerebellumFusion:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.secret_chirp_signature = np.random.randint(100, 999, size=5)
        print(f"[Tales Core] Active Node Online: {self.vehicle_id}")

    def raw_signal_fusion(self, rgb_frame, ultrasonic_matrix):
        h, w, _ = rgb_frame.shape
        fused_spatial_matrix = np.zeros((h, w, 4), dtype=np.float32)
        fused_spatial_matrix[:, :, :3] = rgb_frame
        fused_spatial_matrix[:, :, 3] = ultrasonic_matrix
        return fused_spatial_matrix

    def cerebellum_reflex_filter(self, fused_matrix):
        depth_axis = fused_matrix[:, :, 3]
        critical_forward_zone = depth_axis[30:70, 30:70]
        min_distance = np.min(critical_forward_zone[critical_forward_zone > 0])
        
        if min_distance < 1.5:
            return "TRIGGER_REFLEX_EVADE_AVOID_COLLISION"
        return "ROUTINE_PATH_CLEAR"