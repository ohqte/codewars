def domain_name(url: str) -> str:
    return (
        url.replace("http://", "")
        .replace("https://", "")
        .replace("www.", "")
        .split(".")[0]
    )
