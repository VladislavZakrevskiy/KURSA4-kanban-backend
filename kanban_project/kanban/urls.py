from django.urls import path
from .views.auth_views import register, login, get_profile
from .views.task_views import (
    get_tasks_by_column,
    create_task,
    update_task,
    delete_task,
    move_task,
)
from .views.board_views import (
    create_board,
    delete_board,
    get_board_by_id,
    get_boards,
    update_board,
    share_board,
)

urlpatterns = [
    # Auth
    path("auth/register", register, name="register"),
    path("auth/login", login, name="login"),
    path("auth/profile", get_profile, name="get_profile"),
    # Tasks
    path(
        "tasks/by-column/<str:column_id>/",
        get_tasks_by_column,
        name="get_tasks_by_column",
    ),
    path("tasks/create/", create_task, name="create_task"),
    path("tasks/update/<str:task_id>/", update_task, name="update_task"),
    path("tasks/<str:task_id>/", delete_task, name="delete_task"),
    path("tasks/move-task/<str:task_id>/", move_task, name="move_task"),
    # Board
    # TODO
    path("boards/", get_boards, name="get_boards"),
    path("boards/<int:board_id>/", get_board_by_id, name="get_board_by_id"),
    path("boards/create/", create_board, name="create_board"),
    path("boards/update/<int:board_id>/", update_board, name="update_board"),
    path("boards/delete/<int:board_id>/", delete_board, name="delete_board"),
    path("boards/share/<int:board_id>/", share_board, name="share_board"),
]
