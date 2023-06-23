# Captcha data set

### Data sets so far
- hCaptcha (3795 files)

#### hCaptcha dataset currently only has binary image labelling

### File structure
```
datasets
└── captcha-provider
    ├── category
    │   └── (md5 hash).png
    └── category-negative
        └── (md5 hash).png
```

### ToDo
- [ ] organize all 'negative' categories (feel free to submit a PR if you feel like doing this)
- [ ] add reCAPTCHA