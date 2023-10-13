# Captcha data set

### Data sets so far
- hCaptcha binary (46890 files)
- hCaptcha multiple (568 files)
- hCaptcha text (1519 answers)
- generic text captcha (20000 files)

### File structure
```
datasets
├── hcaptcha
│   ├── binary
│   │   └── category
│   │       ├── true
│   │       │   └── (md5 hash).png
│   │       └── false
│   │           └── (md5 hash).png
│   ├── multiple
│   │   └── category
│   │       └── (md5 hash).png
│   └── text
│       ├── yes.txt
│       └── no.txt
└── generic
    ├── upper
    │   └── (text)-(number).png
    └── lower
        └── (text)-(number).png
```

### ToDo
- [ ] organize all 'negative' categories (feel free to submit a PR if you feel like doing this)
- [ ] add reCAPTCHA
- [x] add hCaptcha multiple choice
- [x] add hCaptcha accessibility text questions (a11y captchas)
- [x] add text-based (image) captchas