
def get_settings_dictionary():
    dict = {}

    dict["default_specs_file"] = "specs/patchnets_generalization_train_on_50_per_category_test_shapenet.json"
    # dict["default_specs_file"] = "specs/patchnets_generalization_train_on_airplanes.json"
    # dict["default_specs_file"] = "specs/patchnets_main_exp.json"
    dict["root_folder"] = "experiment"
  
    return dict

def system_specific_cleanup():
    pass

def system_specific_session_config():
    dict = {}
    return dict