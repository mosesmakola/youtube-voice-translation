from pytube import YouTube
import json

def srt_to_json(srt_text):
    """Converts SRT Caption Format to JSON"""

    captions = []
    lines = srt_text.strip().split("\n\n")

    with open("srt_lines.txt", "w") as f:
        f.write(str(lines))

    for line in lines:
        parts = line.split("\n")
        print(parts)

        if len(parts) >= 3:
            index = parts[0]
            time_range = parts[1]
            text = " ".join(parts[2:])

            start_time, end_time = time_range.split(" --> ")

            captions.append({
                "index": int(index) -1,
                "start_time": start_time,
                "end_time": end_time,
                "text": text
            })
    
    return json.dumps(captions, indent=4, ensure_ascii=False)

def caption_cleaner(caption_json):
    
    with open(caption_json, "r") as file:
        data = json.load(file)

    for row in data:
        print(row["text"])


# https://www.youtube.com/watch?v=nt1SzojVy38

# yt = YouTube(input("Enter YouTube Link: "))

# print(yt.title)

# captions = yt.captions

# print(f"Available Captions: {captions}")

# if "a.en" in captions:
#     english_captions = captions["a.en"]

#     english_srt = english_captions.generate_srt_captions()

#     captions_json = srt_to_json(english_srt)

#     with open("english_captions.json", "w", encoding="utf-8") as file:
#         file.write(captions_json)

#     print("Captions successfully saved to english_captions.json")
# else:
#     print("English captions are not available")


caption_cleaner("english_captions.json")