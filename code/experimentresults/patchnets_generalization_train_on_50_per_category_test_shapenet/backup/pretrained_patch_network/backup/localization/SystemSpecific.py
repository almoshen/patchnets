
def get_settings_dictionary():
    dict = {}

    # dict["default_specs_file"] = "specs/patchnets_main_exp_on_airplanes.json"
    dict["default_specs_file"] = "specs/patchnets_main_exp.json"
    dict["root_folder"] = "experiment"
  
    return dict

def system_specific_cleanup():
    pass

def system_specific_session_config():
    dict = {}
    return dict