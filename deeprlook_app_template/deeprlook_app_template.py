from typing import Any, Dict, List, Tuple

from deeperlook_data_models.data_models.analytics import (ObjectInfo,
                                                          ObjectInfoList)
from vtpl.data_models.app_models import App
from vtpl.data_models.input_zone import ZoneSettings
from vtpl.data_models.job_structure_v200 import Job
from vtpl.data_models.meta_va_event_with_image import MetaVaEventWithImage
from vtpl_api.models.vtpl_video_frame import VtplVideoFrame


class DeeprlookAppTemplate():
    def __init__(self) -> None:
        pass

    def get_result(
        self,
        vtpl_frame: VtplVideoFrame,
        scaled_zones: ZoneSettings,
        obj_info_list: ObjectInfoList,
        track_hist: Dict[float, Any],
        event_res: List[MetaVaEventWithImage],
        app: App,
        process_dl: int,
        obj_detector: Any,
        job: Job,
    ) -> Tuple[List[MetaVaEventWithImage], ObjectInfoList, Dict[float, Any], VtplVideoFrame]:
        event_results: List[MetaVaEventWithImage] = []
        return (event_results, obj_info_list, track_hist, vtpl_frame)

    def stop(self):
        pass
