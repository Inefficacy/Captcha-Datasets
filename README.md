# Captcha data set

### Data sets so far
- hCaptcha binary (53086 files)
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

### this repo will likely never be updated again
