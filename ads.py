ADS = ["📈 YouTube Shorts örnekleri:https://www.youtube.com/@AIDarkTales-3m"
]

def get_ad(count):
    return ADS[count % len(ADS)]
