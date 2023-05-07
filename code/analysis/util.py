''' Adapted from code written by Dexter in stim_notebook.ipynb'''

import numpy as np
import pandas as pd

def language_glm_stim(stim_df, languages1, languages2, tr, n_trs, hrf,
                      block_start_time, block_end_time):
    '''
    Function to construct GLM weights for specific languages
    '''    

    # check languages valid
    lang_list = np.unique(stim_df["Language"])
    assert len(lang_list) == 6
    for l in languages1:
        assert l in lang_list, f"{l} not in {lang_list}"
    for l in languages2:
        assert l in lang_list, f"{l} not in {lang_list}"
    words_per_session = 10
    trials_dict = {}

    # for each language, get the indices of the trials in each session
    for l in lang_list:
        lang_sesh_idx = np.where(stim_df["Language"] == l)[0][::words_per_session] // words_per_session
        assert len(lang_sesh_idx) == 3
        trials_dict[l] = lang_sesh_idx

    # make raster of all languages in languages1 
    languages1_stim_arr = np.zeros(n_trs)
    for l in languages1:
        for start, end in zip(block_start_time[trials_dict[l]], 
                            block_end_time[trials_dict[l]]):
            languages1_stim_arr[int(start / tr): int(end / tr)] = 1

    # make raster of all languages in languages2
    languages2_stim_arr = np.zeros(n_trs)
    for l in languages2:
        if l=='Arabic': # remove last presentation of arabic since cut off 
            trials_dict[l] = trials_dict[l][:-1]

        for start, end in zip(block_start_time[trials_dict[l]], 
                            block_end_time[trials_dict[l]]):
            languages2_stim_arr[int(start / tr): int(end / tr)] = 1

    languages1_stim_conv = np.convolve(languages1_stim_arr, hrf)[:n_trs]
    languages2_stim_conv = np.convolve(languages2_stim_arr, hrf)[:n_trs]

    return languages1_stim_conv, languages2_stim_conv


def make_onset_dur_event_df(stim_df, languages1, languages2, block_start_time, 
                            duration):

    # check languages valid
    lang_list = np.unique(stim_df["Language"])
    assert len(lang_list) == 6
    for l in languages1:
        assert l in lang_list, f"{l} not in {lang_list}"
    for l in languages2:
        assert l in lang_list, f"{l} not in {lang_list}"
    words_per_session = 10
    trials_dict = {}

    # for each language, get the indices of the trials in each session
    for l in lang_list:
        lang_sesh_idx = np.where(stim_df["Language"] == l)[0][::words_per_session] // words_per_session
        assert len(lang_sesh_idx) == 3
        trials_dict[l] = lang_sesh_idx

    trial_type = np.zeros(len(block_start_time))
    for l in languages1:
        for s in trials_dict[l]:
            trial_type[s] = 1
    for l in languages2:
        for s in trials_dict[l]:
            if s==17:
                continue
            trial_type[s] = 2

    trial_type = ['familiar' if i==1 else 'unfamiliar' if i==2 else 'rest' for i in trial_type]

    df = pd.DataFrame({ "onset" : block_start_time, 
                        "duration" : duration,
                        "trial_type" : trial_type})
    return df
