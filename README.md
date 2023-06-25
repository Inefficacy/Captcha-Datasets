# Captcha data set

### Data sets so far
- hCaptcha binary (5503 files)
- hCaptcha multiple (51 files)
- hCaptcha text (703 answers)

### File structure
```
datasets
└── hcaptcha
    ├── binary
    │   ├── category
    │   │   └── (md5 hash).png
    │   └── cateogry-negative
    │       └── (md5 hash).png
    ├── multiple
    │   └── category
    │       └── (md5 hash).png
    └── text
        ├── yes.txt
        └── no.txt
```

### ToDo
- [ ] organize all 'negative' categories (feel free to submit a PR if you feel like doing this)
- [ ] add reCAPTCHA
- [x] add hCaptcha multiple choice
- [x] add hCaptcha accessibility text questions (a11y captchas)
- [ ] add text-based (image) captchas