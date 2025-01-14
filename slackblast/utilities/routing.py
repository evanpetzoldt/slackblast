from utilities import handlers, strava, builders
from utilities.slack import actions


COMMAND_MAPPER = {
    "/backblast": builders.build_backblast_form,
    "/slackblast": builders.build_backblast_form,
    "/preblast": builders.build_preblast_form,
    "/config-slackblast": builders.build_config_form,
}

# Required arguments for view handler functions:
#     body: dict
#     client: WebClient
#     logger: Logger
#     context: dict
VIEW_MAPPER = {
    actions.BACKBLAST_CALLBACK_ID: handlers.handle_backblast_post,
    actions.BACKBLAST_EDIT_CALLBACK_ID: handlers.handle_backblast_post,
    actions.PREBLAST_CALLBACK_ID: handlers.handle_preblast_post,
    actions.PREBLAST_EDIT_CALLBACK_ID: handlers.handle_preblast_post,
    actions.CONFIG_CALLBACK_ID: handlers.handle_config_post,
    actions.STRAVA_MODIFY_CALLBACK_ID: strava.handle_strava_modify,
    actions.CUSTOM_FIELD_ADD_CALLBACK_ID: handlers.handle_custom_field_add,
    actions.CUSTOM_FIELD_MENU_CALLBACK_ID: handlers.handle_custom_field_menu,
}

ACTION_MAPPER = {
    actions.BACKBLAST_EDIT_BUTTON: builders.handle_backblast_edit_button,
    actions.BACKBLAST_NEW_BUTTON: builders.build_backblast_form,
    actions.BACKBLAST_STRAVA_BUTTON: builders.build_strava_form,
    actions.STRAVA_ACTIVITY_BUTTON: builders.build_strava_modify_form,
    actions.BACKBLAST_AO: builders.build_backblast_form,
    actions.BACKBLAST_DATE: builders.build_backblast_form,
    actions.BACKBLAST_Q: builders.build_backblast_form,
    actions.CONFIG_EMAIL_ENABLE: builders.build_config_form,
    actions.STRAVA_CONNECT_BUTTON: builders.ignore_event,
    actions.CONFIG_CUSTOM_FIELDS: builders.build_custom_field_menu,
    actions.CUSTOM_FIELD_ADD: builders.build_custom_field_add_edit,
    actions.CUSTOM_FIELD_EDIT: builders.build_custom_field_add_edit,
    actions.CUSTOM_FIELD_DELETE: builders.delete_custom_field,
    actions.PREBLAST_NEW_BUTTON: builders.build_preblast_form,
    actions.PREBLAST_EDIT_BUTTON: builders.handle_preblast_edit_button,
}

VIEW_CLOSED_MAPPER = {
    actions.CUSTOM_FIELD_ADD_FORM: builders.ignore_event,
    actions.STRAVA_MODIFY_CALLBACK_ID: strava.handle_strava_modify,
}

MAIN_MAPPER = {
    "command": COMMAND_MAPPER,
    "block_actions": ACTION_MAPPER,
    "view_submission": VIEW_MAPPER,
    "view_closed": VIEW_CLOSED_MAPPER,
}
