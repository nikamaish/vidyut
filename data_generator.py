def generate_random_data():
    data = []
    main_entry_names = ['entry_name_1', 'entry_name_2', 'entry_name_3', 'entry_name_4', 'entry_name_5']
    for name in main_entry_names:
        main_entry = {
            'main_entry_id': name
        }
        data.append(main_entry)
    return {'data': data}
