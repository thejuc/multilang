## NEU 502B Final project - Multi langauge perception with fMRI data

Group members: Will Long, Iman Wahle, Dexter Tsin, Yousuf El-jayyousi, Sae Yokoyama

Analysis code for NEU 502B final project.

Checklist 
- [x] `code/analysis/preprocess_notebook.ipynb`
    - [x] Head motion error
    - [x] acompCor (`n_components = 5`)
    - [x] Framewise displacement (`threshold = 0.25`)
    - [x] Confounds array at: `/jukebox/PNI-classes/students/NEU502/2023-NEU502B/wlong/multilang/preprocessed_data/confounds.npy`

- [x] `code/analsis/stim_notebook.ipynb`
    - [x] Basic block stimulus with glover hrf
    - [x] block stimiulus with specific language
    - [x] Stim array at: `/jukebox/PNI-classes/students/NEU502/2023-NEU502B/wlong/multilang/preprocessed_data/stim_arr.npy`

- [x] `code/analysis/GLM_notebook.ipynb`
    - [x] Basic OLS regression with confounds
    - [x] Basic OLS regression with time-lagged stimulus
    - [x] Regression analysis with `FirstLevelModel` from `nilearn`
    
    
TODO

- [x] figure 1
    - [x] figure of task
    
- [x] figure 2
    - [x] anatomy for both subjects
    - [x] auditory mask
    - [x] mean bold signal in auditory cortex
    - [x] preprocessing (head motion, etc)

- [x] figure 3
    - [x] GLM coef on brain for familiar language vs not
    - [x] GLM coef on brain for first language vs second
    
- [x] figure 4
    - [x] Word embeddings (optional)
