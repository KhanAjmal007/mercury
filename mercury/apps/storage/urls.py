from django.urls import re_path

from apps.storage.views.dashboardfiles import (
    GetStorageType,
    DeleteFile,
    FileUploaded,
    ListFiles,
    PresignedUrl,
    PresignedUrlPut,
)
from apps.storage.views.workerfiles import (
    WorkerAddFile,
    WorkerGetUploadedFilesUrls,
    WorkerPresignedUrl,
)
from apps.storage.views.notebookfiles import (
    NbPresignedUrlPut,
    NbFileUploaded,
    NbDeleteFile,
    WorkerGetNbFileUrl,
)

storage_urlpatterns = [
    re_path(
        "api/v1/storage-type",
        GetStorageType.as_view(),
    ),
    #
    # dashboard files
    #
    re_path("api/v1/(?P<site_id>.+)/files", ListFiles.as_view()),
    re_path(
        "api/v1/presigned-url/(?P<action>.+)/(?P<site_id>.+)/(?P<filename>.+)",
        PresignedUrl.as_view(),
    ),
    re_path(
        "api/v1/presigned-url-put/(?P<site_id>.+)/(?P<filename>.+)/(?P<filesize>.+)",
        PresignedUrlPut.as_view(),
    ),
    re_path(
        "api/v1/file-uploaded",
        FileUploaded.as_view(),
    ),
    re_path(
        "api/v1/delete-file",
        DeleteFile.as_view(),
    ),
    #
    # style files
    #
    re_path(
        "api/v1/style-put/(?P<site_id>.+)/(?P<filename>.+)/(?P<filesize>.+)",
        PresignedUrlPut.as_view(),
    ),
    re_path(
        "api/v1/style-get/(?P<site_id>.+)/(?P<filename>.+)",
        PresignedUrlPut.as_view(),
    ),
    #
    # worker files
    #
    re_path(
        "api/v1/worker/presigned-url/(?P<action>.+)/(?P<session_id>.+)/(?P<worker_id>.+)/(?P<notebook_id>.+)/(?P<output_dir>.+)/(?P<filename>.+)",
        WorkerPresignedUrl.as_view(),
    ),
    re_path(
        "api/v1/worker/add-file",
        WorkerAddFile.as_view(),
    ),
    re_path(
        "api/v1/worker/uploaded-files-urls/(?P<session_id>.+)/(?P<worker_id>.+)/(?P<notebook_id>.+)",
        WorkerGetUploadedFilesUrls.as_view(),
    ),
    # user uploaded files in notebooks
    re_path(
        "api/v1/nb-file-put/(?P<site_id>.+)/(?P<session_id>.+)/(?P<filename>.+)/(?P<filesize>.+)",
        NbPresignedUrlPut.as_view(),
    ),
    re_path(
        "api/v1/nb-file-uploaded",
        NbFileUploaded.as_view(),
    ),
    re_path(
        "api/v1/nb-delete-file",
        NbDeleteFile.as_view(),
    ),
    re_path(
        "api/v1/worker/user-uploaded-file/(?P<session_id>.+)/(?P<worker_id>.+)/(?P<notebook_id>.+)/(?P<filename>.+)",
        WorkerGetNbFileUrl.as_view(),
    ),
]
