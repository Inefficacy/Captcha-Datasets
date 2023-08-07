# Captcha data set

### Data sets so far
- hCaptcha binary (25767 files)
- hCaptcha multiple (568 files)
- hCaptcha text (1512 answers)
- generic text captcha (20000 files)

### File structure
```
datasets
├── hcaptcha
│   ├── binary
│   │   ├── category
│   │   │   └── (md5 hash).png
│   │   └── cateogry-negative
│   │       └── (md5 hash).png
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