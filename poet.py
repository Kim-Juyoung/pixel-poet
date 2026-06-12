#!/usr/bin/env python3
import random
import re
import textwrap

TEMPLATES = [
    [
        "{w0}은 어디서 왔을까",
        "{w1}이 지나간 자리마다",
        "아무도 모르게",
        "{w2}이 피어났다",
    ],
    [
        "한 줌의 {w0}을 쥐고",
        "나는 {w1} 쪽으로 걸었다",
        "뒤돌아보니",
        "그곳엔 {w2}만 남아 있었다",
    ],
    [
        "{w2}이 먼저 도착해 있었다",
        "그 다음엔 {w0}이",
        "마지막으로 {w1}이 왔고",
        "우리는 서로를 오래 바라보았다",
    ],
    [
        "{w0}에게 물었다",
        "{w1}은 어디 있냐고",
        "대답 대신",
        "{w2}이 내 손을 잡았다",
    ],
    [
        "오늘 밤 {w1}은",
        "{w0}의 꿈을 꿀 것이다",
        "내일 아침",
        "{w2}이 그 꿈을 데려갈 때까지",
    ],
    [
        "{w0}도 울 때가 있다",
        "아무도 보지 않는 곳에서",
        "{w2}처럼 조용히",
        "{w1}을 그리워하며",
    ],
    [
        "처음엔 {w0}이었다",
        "그다음엔 {w1}이 되었고",
        "결국 나는",
        "{w2}이 되어버렸다",
    ],
    [
        "{w1}과 {w2} 사이 어딘가에",
        "길을 잃은 {w0} 하나",
        "집으로 가는 길을",
        "아직 찾고 있다",
    ],
    [
        "봄이 오면 {w0}이 생각나고",
        "여름이 지나면 {w1}이 그립다",
        "가을엔 {w2}을 기다리다",
        "겨울에 혼자 웃는다",
    ],
    [
        "{w0}을 잊으려 했는데",
        "{w1}이 자꾸 떠오르고",
        "결국 {w2} 앞에 서서",
        "아무 말도 못 했다",
    ],
]

FRAMES = [
    # 클래식
    lambda lines, w: [
        "╔" + "═" * (w + 2) + "╗",
        *["║ " + l.center(w) + " ║" for l in lines],
        "╚" + "═" * (w + 2) + "╝",
    ],
    # 별
    lambda lines, w: [
        "✦ " + "·" * (w + 2) + " ✦",
        *["· " + l.center(w) + " ·" for l in lines],
        "✦ " + "·" * (w + 2) + " ✦",
    ],
    # 꽃
    lambda lines, w: [
        "❀ " + "~" * (w + 2) + " ❀",
        *["~ " + l.center(w) + " ~" for l in lines],
        "❀ " + "~" * (w + 2) + " ❀",
    ],
    # 달
    lambda lines, w: [
        "☽ " + "━" * (w + 2) + " ☾",
        *["│ " + l.center(w) + " │" for l in lines],
        "☽ " + "━" * (w + 2) + " ☾",
    ],
]

def make_poem(words):
    w0, w1, w2 = words[0], words[1], words[2]
    template = random.choice(TEMPLATES)
    return [line.format(w0=w0, w1=w1, w2=w2) for line in template]

def frame_poem(lines):
    width = max(len(l) for l in lines) + 4
    frame = random.choice(FRAMES)
    return frame(lines, width)

def print_colored(lines):
    colors = ["\033[95m", "\033[94m", "\033[96m", "\033[92m", "\033[93m"]
    reset = "\033[0m"
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        print(color + line + reset)

def main():
    print("\033[1m\033[93m")
    print("  ╔══════════════════╗")
    print("  ║   🌸 픽셀 시인 🌸  ║")
    print("  ╚══════════════════╝")
    print("\033[0m")
    print("단어 세 개를 입력하면, 시를 써드립니다.\n")

    while True:
        try:
            raw = input("단어 세 개를 입력하세요 (쉼표로 구분, 예: 바람,별,강): ").strip()
            if not raw:
                continue
            words = [w.strip() for w in re.split(r'[,，\s]+', raw) if w.strip()]
            if len(words) < 3:
                print("→ 단어를 세 개 입력해주세요!\n")
                continue

            words = words[:3]
            poem_lines = make_poem(words)
            framed = frame_poem(poem_lines)

            print()
            print_colored(framed)
            print()

            again = input("다시 써볼까요? (y/n): ").strip().lower()
            if again != "y":
                print("\n\033[93m시가 당신의 하루를 물들이길 바랍니다. 🌸\033[0m\n")
                break
            print()

        except KeyboardInterrupt:
            print("\n\n\033[93m안녕히 가세요. 🌸\033[0m\n")
            break

if __name__ == "__main__":
    main()
