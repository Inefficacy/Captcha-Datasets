# Captcha data set

### Data sets so far
- hCaptcha binary (5295 files)
- hCaptcha text (119 answers)

#### hCaptcha dataset currently only has binary image labelling

### File structure
```
datasets
└── hcaptcha
    ├── binary
    │   ├── category
    │   │   └── (md5 hash).png
    │   └── cateogry-negative
    │       └── (md5 hash).png
    └── text
        ├── yes.txt
        └── no.txt
```

### ToDo
- [ ] organize all 'negative' categories (feel free to submit a PR if you feel like doing this)
- [ ] add reCAPTCHA
- [ ] add hCaptcha multiple choice
- [x] add hCaptcha accessibility text questions (a11y captchas)