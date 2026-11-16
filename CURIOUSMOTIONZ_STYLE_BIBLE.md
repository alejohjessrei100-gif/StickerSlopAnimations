# CURIOUSMOTIONZ — COMPLETE CREATIVE STYLE BIBLE

*Reverse-engineered from the channel's actual Shorts. Version 1.0 — research date 2026-11-16.*

---

## 0. EVIDENCE BASE & LIMITATIONS (read first)

**What I actually did**
- Pulled the full public Shorts list of the channel (handle `@curiousmotionz`, display name "curiousmotions", ~6.09K subscribers): **17 Shorts, all uploaded 2026-10-27 → 2026-11-13** (~1 per day).
- For **all 17** I downloaded YouTube's own storyboard frame sheets (≈1 frame per second, 101×180 px) and rebuilt them as contact sheets: `reference/contact-sheets/<videoId>.png`. I read every one of them visually (captions, characters, props, backgrounds, scene changes).
- Pulled per-video metadata: title, duration, views, likes, comments, upload date, description.
- Measured scene-change rate by frame-differencing the 1 fps frames.

**What I could NOT do (hard limits, no pretending)**
| Not possible | Why | Consequence |
|---|---|---|
| Watch the videos at full resolution / full frame-rate | YouTube returned "Sign in to confirm you're not a bot" for every video-stream request from this server | Motion analysis is from 1-second samples + inference. Easing curves, sub-second animation, exact transition type = **inferred, not confirmed**. |
| Hear any audio | Same block; no captions/transcripts exist on the videos | **Voice, music, SFX, mixing are NOT observed.** Section 8 is a recommended spec, clearly marked as such. |
| Read exact scripts | No transcripts | Scripts are **reconstructed** from burned-in caption words visible in frames + the descriptions (which for ~12 videos are written summaries). |
| Browse Pinterest | Pinterest search is a JS app; returns an empty shell to my server | I give you **search keywords and ready-made search URLs**, not verified pins. Untested. |
| See YouTube Analytics | Private | All "why it works" statements are labeled **[Hypothesis]**. Only public view/like numbers are used. |

Label key used throughout: **[OBSERVED]** = seen in frames/metadata. **[INFERRED]** = strong deduction from frames. **[HYPOTHESIS]** = my reasoning about why. **[SPEC]** = my recommendation, not observed.

**Do this 20-minute verification pass yourself** (the things I couldn't see): watch 3 Shorts with sound and note (1) voice type (human/TTS), gender, pace; (2) is there music, what genre, how loud; (3) the SFX on pop-ins (whoosh/pop/ding?); (4) exact caption font (screenshot to a font-identifier); (5) whether the last frame loops back to the first. Then update §8 and §3E.

---

## 1. CHANNEL IDENTITY & CREATIVE DIRECTION

**One-line identity [OBSERVED]:** *"Weird true food/brand stories, told in ~38 seconds, acted out by a cartoon-headed cast in photoreal collage scenes, with a new picture every ~1.7 seconds."*

**Fixed format [OBSERVED]**
- 9:16 Shorts, 28–50 s (mean 38.6 s).
- Niche: food + brands + history oddities ("#food #history #shorts"). Includes non-food brand stories (Nintendo, Tesla).
- Title formula: **`[Entity] [emotional/ironic verb] [odd specific thing] 😯[topic emoji]`**
  - "Nintendo Regrets Suing This Guy 😯🎮", "Tesla Regrets Ghosting This Bakery 😯🥧", "Burger King Offered $5,000 To Find This Guy 😯🍔", "When Italy Tried To BAN Pasta 😯🍝".
  - Every title but one carries **😯 + one topical emoji** — a brand marker.
  - Verbs that recur: *Regrets, Offered, Saved, Used To (give/pay), Banned, Conquered, Invented, Found.*
- Description [OBSERVED]: 2–4 sentences, plain summary, ends with *"The story of …"* / *"The true story of …"*, then `#food #history #shorts`.

**Creative promise to the viewer:** "You will learn one absurd-but-true thing in under 40 seconds and it will have a twist."

**Tone [INFERRED]:** deadpan-playful. Cartoon faces + gags (money rain, ☠️ thought bubbles, stars) keep it light even for dark topics (death-row twins, a man found after a stroke).

**Performance snapshot [OBSERVED, public numbers]**
- Total across 17 Shorts ≈ **7.89M views**. Median ≈ **110K**. One outlier ("How North Korea Invented Fast Foods", 4.65M views, 117K likes) = **59%** of all views. Treat the channel as *one breakout + a solid 400–640K tier + a long tail of 16–70K*.
- Tier 1 (>400K): King's coffee/tea experiment, Nashville hot chicken revenge, Burger King "Herb" $5,000, Nintendo/Super Mario store.
- Long tail (16–50K): corporate promo stories — Domino's tattoo, White Castle burger diet, BK 1-cent Whoppers, bread ban, noodle shop drug test, sushi names.
- **[HYPOTHESIS]** Stories with a *person at stake* (death sentence, revenge, a life saved, David-vs-Goliath) beat stories that are *a brand doing a promo*. Use this as a topic-selection filter (§10).

---

## 2. VISUAL IDENTITY

### 2A. The signature look [OBSERVED]
**"Cartoon-head-on-photo-body" collage.** Every scene is built from three layers:
1. **Background** — a photoreal (looks AI-generated or heavily stock-edited) environment: kitchen, bakery, courtroom, street, prison, Burger King interior, Statue of Liberty, map.
2. **Character(s)** — full-body **photographic-looking bodies and clothes** (chef whites, ermine robe, denim jacket, Soviet-style green uniform) topped with a **flat vector cartoon head**: big round skull, small eyes, thin dark outline, simple cell-shaded skin, *very* expressive mouth/brows. Think Bitmoji/Memoji head pasted on a real body.
3. **Props / graphics** — photoreal cutouts (pizza, whopper, phone, calendar, document, tombstones) or flat graphics (red X, ⭐, "BANNED" stamp, VS slash, "?" bubble).

Then **captions** sit on top (§5).

### 2B. Character design rules [OBSERVED → rules]
- **Head**: skin-toned cartoon oval, ~⅕–¼ of the body height (slightly oversized), thin dark outline, mild shading. Eyes: simple white ovals with small pupils; eyebrows carry the emotion.
- **Expression set seen across videos**: neutral/deadpan, wide-open laughing mouth, shocked ("O" mouth, brows up), angry (red face + steam puffs), sad/crying (teal tears — Tesla baker), sleepy ("z" bubbles — bread baker), disgusted/green (nauseated White Castle customer), stars-in-eyes/happy.
- **Body**: photoreal, standing, usually **frontal or ¾**, arms often in a *signature pose* (hands on hips, arms crossed, one arm pointing, both arms up celebrating, holding a prop).
- **Costume = identity.** The cast stays in the *same outfit for the whole video* so viewers track "who is who": King = white ermine robe + blue sash + crown; Twin = off-white shirt, barefoot; Herb = black silhouette head with "?"; Bakery owner = black apron; Tesla exec = black jacket/dark suit.
- **Role colors**: heroes in warm/saturated clothing (red, blue, green); authority figures in dark/uniform colors (black, olive). **[INFERRED]**
- **Mystery character trick**: when someone is unknown/unseen, the head is a **black silhouette with a white "?"** (Herb; "the woman nobody can name"). Reuse this for any unknown.
- **Real people** (Elon, Kim Jong-un, Mussolini, Gustav III) are shown with a *caricatured cartoon head* on a costume body, not a photo.
- **Crowd**: duplicated mini cartoon heads in a row (Nashville "women" line-up; Tesla bakery customers).

### 2C. Backgrounds & color [OBSERVED]
- **One dominant color field per scene, changing every beat**: green kitchen → magenta/night → navy sky → red diner → teal window. Large, flat-ish color zones behind the character guarantee figure/ground separation at phone size.
- **Period/archive topics go monochrome**: White Castle (B&W 1930s street, B&W lab) and the WW2 bread video (grayscale London, bombed St Paul's) use **desaturated backgrounds with the colored cartoon character popping on top**. Rule: *past = grayscale/sepia world, character stays colored.* Modern topics = full saturation.
- **Map and "world" shots**: stylized atlas (Italy, Korea), night-lights USA map, flat green-states map that fills with burger icons.
- **Lighting**: mostly soft, even, "stock-photo" light; occasional dramatic scenes get a spotlight or neon (magenta storefront at night with a moon; Herb in a stage spotlight with a red curtain). The cartoon head has no cast shadow — a **soft contact shadow under the feet** (or none) is enough.
- **Composition [OBSERVED]**: character **centered**, feet close to the bottom third, head in the upper-middle (roughly 35–55% of frame height). The **top 25–30% is background/sky/architecture (a "sign zone")** where flags, signs, speech bubbles, years and thought bubbles appear. **Captions sit in the lower-middle over the character's legs/waist.**
- **Depth**: foreground prop (checkered tablecloth, desk, counter, podium) overlaps the character's lower body → fakes 3D layering. Seen in Nashville breakfast table, Tesla bakery counter, Bread Order desk, Nintendo shop counter.

### 2D. The prop/graphic vocabulary [OBSERVED] — build this as your sticker library
| Prop | Used for | Example |
|---|---|---|
| Smartphone with chat bubbles | messages, announcements, orders | Tesla cancel text; Sushiro group chat |
| Calendar page (flips date/day) | time passing, deadlines | "FEB 20 → 21" Tesla; "DAY 1" doctors; "MARCH 2021" sushi |
| Document / invoice / newspaper / ID card / form | proof, rules, laws | "THE BREAD ORDER", "THE DEAL" scroll, "THE DAILY NEWS", Taiwan ID, name-change form with APPROVED stamps |
| Red ❌ over an object | banned / rejected / cancelled | crossed-out Super Mario sign; "ANTI-PASTA" poster; banned bread shelves |
| Red "BANNED" / green "APPROVED" stamp | rule outcome | woman drinking coffee + BANNED stamp |
| Prohibition sign 🚫 | forbidden thing | "Spaghetti is unpatriotic" poster |
| Yellow ⭐ ×1–3 | success / great idea | stars appear above the head when the hero wins |
| Thought bubble with emoji | what a character believes/plans | ☕ → ☠️ ("coffee is slow poison"), 🍕🍔 over Kim |
| Falling items (money 💵, cookies, papers) | abundance / overwhelm | $ rain (BK $5,000); 2,000 cookies; flurry of legal documents |
| Counters/overlays (WEEK 2/6/10/11, 24 burgers, Age 38/64/83, 1974/1984/1985, 70 YEARS) | numbers & time | pile of burgers grows with week counter |
| VS split screen | duel / experiment | COFFEE vs TEA with a red slash "VS" |
| "?" in a black silhouette head | unknown person | Herb, unnamed Nashville woman |
| Map with fills | spread / scale | states filling with burger icons |
| Speech bubble with short quote | the line that matters | "I'm not Herb" |
| Emojis 💀🍔 in bubbles | comedic emphasis | White Castle skull bubble |

---

## 3. ANIMATION & MOTION

> Reminder: sampled at 1 fps. What follows is **[OBSERVED]** where I saw before/after states in consecutive frames, **[INFERRED]** for the motion between them.

### 3A. The motion grammar
1. **Character push-in (scale up).** Consecutive frames show the same couple/character larger in the next second (Nashville "had stayed → night"; Domino's frame 10→11 jumps to a huge close-up of a face for "is when"). Rule: *every character shot slowly scales ~100% → 110–125% during its life (Ken-Burns on the cutout), and occasionally hard-cuts to an extreme close-up of the face for emphasis.*
2. **Pose swaps, not full rigging.** The body changes pose between beats (arms down → arms up → pointing) and the mouth/brows change expression. **[INFERRED]** this is done by swapping alternate cutout poses/heads, not by a skeleton.
3. **Prop pop-in.** A prop appears in front of the character between seconds (table with tablecloth at "came home"; stacked paper pile growing; pizza on the red tablecloth). **[INFERRED]** scale 0 → 110% → 100% "overshoot pop", 6–10 frames.
4. **Falling/raining objects.** Cookies, dollar bills, paper sheets falling → particle-style loops for abundance/chaos.
5. **Counters & stamps.** Numbers tick; stamps slam on (scale 150% → 100% with a tiny rotation).
6. **Background camera move.** Backgrounds are not static — slow zoom or drift (Tesla bakery wide → closer; city streets). **[INFERRED]** 100→108% over ~2 s.
7. **Scene change = hard cut on the beat**, not dissolves. The measured **average time between background changes = 1.69 s** (range 1.33–2.14 s across the 17 Shorts; method: frame-diff of the top region at 1 fps — underestimates sub-second cuts).
8. **Within a scene, something else changes every ~0.5–1 s**: caption chunk, expression, prop, bubble, star, counter.
9. **Parallax/layering**: foreground table/desk, mid character, background room → give the 3 layers slightly different scale-up speeds (fg fastest). **[SPEC — consistent with observed layering]**
10. **Reveal by silhouette**: black head "?" → reveal real cartoon head (Herb: unknown → shown at the Super Bowl TV).

### 3B. How the channel avoids static visuals [OBSERVED]
- Never holds the same picture >2 s except for deliberate emphasis frames.
- Alternates **wide (character full-body in room)** ↔ **insert (phone, document, calendar, food)** ↔ **map/establishing** ↔ **close-up (face)**. Pattern roughly: *character → insert → character → map → character → insert*.
- Every sentence introduces a **new noun that gets its own visual** (see "one noun = one visual", §9).

### 3C. Recreating it in an editor (CapCut / Premiere / After Effects / DaVinci)
**Per scene (every ~1.7 s) build this stack:**
```
V5  Captions (3-word chunks)                  ← top layer
V4  Overlays: stars, ❌, stamp, bubble, $ rain, counter
V3  Foreground prop (table/desk/counter)      ← scale 100→112% (fastest)
V2  Character cutout (cartoon head + body)    ← scale 100→110%, ±1° rotation wobble
V1  Background (photoreal / map)              ← scale 100→106% (slowest)
```
- **Pop-in preset** (save as a template): Scale 0→108% (4 frames, ease-out) → 100% (4 frames, ease-in-out); Opacity 0→100% in first 2 frames. 30 fps.
- **Slam stamp preset**: Scale 160→100% in 5 frames, rotation −8°→−4°, subtle shake 2 frames.
- **Character idle**: scale 100→110% linear over the clip duration; 1–2° rotation oscillation ("breathing").
- **Hard cut** on the first syllable of the new sentence. No cross-dissolves.
- **Mouth/expression swaps**: prepare 3 heads per character (neutral / open-mouth / reaction) and cut between them at emphasis words.

---

## 4. EDITING & PACING

**[OBSERVED]**
| Metric | Value |
|---|---|
| Length | 28–50 s, mean 38.6 s |
| Background/scene change | every ~1.7 s (1.33–2.14 s) → **~20–32 scene changes per Short** |
| Visual change of any kind | at least once per second in the sampled frames |
| Caption chunk | 1–3 words, new chunk ≈ every second in samples (probably faster; see below) |
| Transitions | hard cuts; no visible dissolves/wipes in any sampled frame |
| Opening | main character or hook object is in frame at **t = 0**, already captioned |
| Ending | the final frames are the payoff image (e.g., "dead" over the prison yard; Domino's rescued man + two delivery guys) — **no outro card seen** (last frame was partial in the storyboard — can't confirm a loop) |

**Pattern interrupts [OBSERVED]**: scale jump to extreme face close-up; sudden switch to B&W/archival photo; phone screen insert; money/paper rain; VS split; red ❌; stars; zoom to a map; "?" silhouette.

**Pacing rules [SPEC derived from above]**
1. ≤2.0 s per scene, target 1.5 s.
2. After 3 character scenes, force an **insert** (phone/document/food/map).
3. Every ~8–10 s put one "wow beat" with a big overlay (money rain, VS, stamp slam, giant number).
4. Never repeat the same background twice in a row; **return** to the hero's home background only to mark a callback.

**Sound design** → not observed; see §8.

---

## 5. TYPOGRAPHY & CAPTIONS

**[OBSERVED]**
- **One style, all videos**: white, bold, **rounded casual "comic" sans** (Comic-Neue / Chewy-family feel), **thick black outline** (≈ 6–8% of cap height) + light drop shadow. No background boxes.
- **Size**: small-to-medium — cap height roughly 2.5–3% of frame height (≈ 45–55 px on a 1920 canvas). Not a mega-bold TikTok caption. Because it's small, **the visual does the shouting, the caption just confirms.**
- **Chunking**: **1–3 words at a time** (e.g., "Burger", "said I'm", "not Herb"). Lower-case/sentence-case, no all-caps, no emoji in captions.
- **Position**: horizontally centered; **vertically in the lower-middle** (≈ 60–80% of frame height — over the character's torso/legs). It *moves a little* depending on the scene so it doesn't hide the key prop (higher over tall characters, near the bottom on the full-body shots). Stays out of the bottom ~12% (YouTube UI zone).
- **Animation [INFERRED]**: word-synced chunk swaps; I could not see a scale-pop on each chunk or colored keyword highlights in the sampled frames — **verify**.
- **Diegetic text**: in-world typography does the heavy lifting — "YEARS OPEN 70", "MUST BE 16", "NASHVILLE CITY LIMIT", "THE BREAD ORDER", "NOT COVERED", "WEEK 11". These use **different fonts** (sign fonts, newspaper serif, system UI on phones), which creates variety *without* changing the caption style.

**Spec to copy** [SPEC]
```
Font: Comic Neue Bold / Fredoka SemiBold (free, Google Fonts)
Size: 52 px @ 1080×1920, line max 3 words
Fill #FFFFFF, stroke #000000 7px (outside), shadow #000 60% 0/3px blur 2
Position: x center, y 1230–1480 px, nudge ±150 px to avoid covering the prop
Keep-out: bottom 230 px, right 130 px
Highlight (optional, my addition): key number/noun → #FFD84D for that chunk only
```

---

## 6. ASSET SOURCING & PINTEREST GUIDE

**Honesty note:** I couldn't browse Pinterest, so I did **not** verify specific pins match. The search strings below are built from what I saw on screen. **Open each search URL, judge against the "accept/reject" tests, and save only passes.** Search URL pattern:
`https://www.pinterest.com/search/pins/?q=<URL-encoded keywords>`

### 6.1 The most important decision: copyright & platform risk
- Pinterest images are mostly **other people's copyrighted work**. For a monetized channel, cutouts of unlicensed pins are a takedown/demonetization risk. Safer ladder: **(1) AI-generated assets you own/license → (2) licensed stock/free-license sites → (3) Pinterest only as *reference* and for public-domain/free-license items.**
- The channel's look (photoreal backgrounds with a slightly "AI-clean" sheen, bodies in perfectly clean costumes, one-off scenes like "Statue of Liberty with a chili flame") strongly suggests **AI-generated backgrounds and bodies** **[HYPOTHESIS — I can't prove the tool]**. Replicating with an image generator gives you consistency *and* ownership.
- YouTube's "inauthentic / mass-produced content" policy targets repetitive templated uploads with little original value. Your protection is **original scripts, original research, original arrangement** — which is what this system is designed for.

### 6.2 Asset categories, keywords, and tests

**A. Backgrounds (photoreal environments, 9:16, character-free, with empty floor space)**
- Keywords: `empty kitchen interior vertical`, `bakery shop interior photo`, `1930s street black and white photograph`, `courtroom interior`, `prison cell stone interior`, `fast food restaurant interior red booth`, `suburban house front porch`, `london street 1940s`, `statue of liberty blue sky vertical`, `vintage atlas map italy`, `phone screen mockup chat`, `green road sign mockup`.
- Accept if: horizon/floor line in the **lower 40%**, empty centre, **dominant single hue**, soft light, no people, ≥1080×1920 or upscalable.
- Reject: busy centre, strong cast shadows, text/logos you can't clear, tilted camera.
- Prep: crop/scale to 1080×1920 with extra 10% margin for push-in; for historic topics **desaturate to B&W/sepia**; punch contrast.

**B. Full-body "costume bodies" (the cast)** — headless or head-removable
- Keywords: `full body standing man transparent png`, `chef full body png`, `king ermine robe costume`, `businessman suit full body png`, `delivery driver uniform full body`, `woman apron full body png`, `1940s policeman costume`, `medieval prisoner shirt`, `character reference sheet standing front view`, `fashion lookbook full body front facing`.
- Accept if: **frontal/¾ pose, arms away from torso, feet visible, neck visible, plain background (easy cut)**, clothes fit the role/era, high resolution.
- Reject: arms crossing the neck/face, hair covering the neck, cropped feet, heavy motion blur.
- Prep: remove background → **erase the head** (leave neck) → place cartoon head (§6.4).
- Build a **Role Library**: `chef, baker, king, soldier/officer, doctor, scientist, delivery-driver (red/blue), cashier, politician, CEO (black jacket), lawyer, judge, policeman, prisoner, shopper, kid, grandma`. Each in 2–3 poses (neutral, arms-up, pointing). This is your reusable cast.

**C. Props (photoreal cutouts)**
- Keywords: `[food] transparent png` (pizza, burger, whopper, fried chicken skillet, pasta plate, croissant, bread loaf, sushi plate, noodle bowl), `smartphone in hand transparent png`, `hand holding phone mockup`, `wall calendar page`, `old paper document png`, `wax seal scroll png`, `newspaper front page mockup`, `stack of papers png`, `money cash falling png`, `skull png`, `tombstone png`, `gallows`, `copper pots`, `teapot`, `microphone`, `easel`.
- Accept: clean alpha edges (no white halo), 3/4 top-down view for tabletop foods, strong saturation (food must look *delicious*).
- Prep: cutout → 2 px feather → add **soft contact shadow** under it → export PNG with trim.

**D. Graphic stickers (flat/2D)**
- Keywords: `red x png`, `banned stamp png`, `approved stamp png`, `prohibition sign png`, `gold star png`, `thought bubble png`, `speech bubble comic png`, `question mark png`, `vs lightning png`, `dollar bill png`, `arrow hand drawn png`, `flag of [country] waving png`, `calendar date png`, `green road sign png`.
- Accept: bold, saturated, **thick outline**, readable at 120 px.

**E. Cartoon heads (the signature element)**
- Look-alike search: `bitmoji style avatar`, `memoji style face vector`, `flat cartoon head transparent png`, `cartoon face expressions pack`, `avatar maker free`. **Build, don't scrape**: make 6–8 base heads (skin tones × age × gender) in a vector tool or avatar maker you have the right to use, each with **expression variants** (neutral, laugh, shock, anger, sad, sleepy, smug, "?" silhouette).
- Style lock: outline 3–4 px dark brown, 2-tone shading, eyes = white ovals + black dot, brows thick, mouth = filled shape with teeth only on laughs.

**F. Archival/period photos** (for 1930s/1940s)
- Keywords: `1930s street photo`, `1940s bread queue`, `vintage newspaper front page 1985`. Prefer public-domain archives (Library of Congress, Wikimedia Commons). Convert to B&W.

**G. Real-world cutouts: logos/brands/products**
- Brands (Burger King, Domino's, Tesla, KFC, Nintendo) appear as signage and products. **Legal note:** nominative use for commentary is common but not risk-free; avoid implying endorsement, don't use logos as your own branding.

### 6.3 Background removal & prep workflow
1. **Cutout**: remove.bg / Photoshop *Select Subject* / CapCut *Auto cutout* / Canva *BG Remover* / local `rembg` (U²-Net). Clean fringe: Select → Modify → Contract 1–2 px → Feather 1 px.
2. **Name & store** as `ROLE_pose_variant.png` (e.g., `KING_front_neutral.png`); keep a Pinterest/source URL + license column in a spreadsheet.
3. **Normalize**: height of full-body cutouts = **1100 px** on a 1080×1920 canvas; baseline feet at y≈1550; props max 450 px wide.
4. **Colour match**: lift shadows on cutouts, add the background's dominant hue as a faint rim light (5–10%).
5. **Soft shadow**: black ellipse, 35% opacity, blur 12, under feet.

### 6.4 Attaching the cartoon head
1. Erase photo head, keep neck.
2. Place cartoon head so the chin overlaps the neck by ~15%; scale head height ≈ 22% of body height (slightly big = the look).
3. Match skin tone to the neck/hands (colour-pick), add a thin darker line at the chin join.
4. Keep **expression variants as separate PNGs** with identical anchor point so swaps don't jump.

### 6.5 Consistency between videos
- A **Palette sheet** (§7), a **font setting** (§5), a **Cast bible** (each recurring role = fixed outfit colour + head), a **prop library**, and **one caption preset** = the five locks. Never change them per video. Change only background/topic.

---

## 7. VISUAL SYSTEM QUICK SHEET

| Token | Value |
|---|---|
| Canvas | 1080×1920, 30 fps |
| Safe area | keep key content within x 60–1020, y 220–1620 |
| Character | centre-x 540, height ~1000–1100 px, feet y≈1550 |
| Caption zone | y 1230–1480 |
| Sign zone | y 120–520 (flags, years, bubbles, headlines) |
| Palette anchors (sampled by eye) | forest green `#1F5E3A`, magenta `#C2185B`, night navy `#101B4D`, sky blue `#2D7DD2`, diner red `#C62828`, teal `#1F8A8A`, warm cream `#F3E6CC`, gold star `#FFD84D` |
| Rule | **one dominant hue per scene**, adjacent scenes must differ in hue by ≥60° or in brightness by ≥30% |
| Period rule | pre-1990 world scenes → B&W/sepia background, hero in colour |

---

## 8. AUDIO & NARRATION — **ENTIRELY [SPEC], NOT OBSERVED**

I could not hear any audio. Below is what the *visuals imply* plus a safe spec. Replace with observations after your verification pass.

- **Pacing implied by captions**: 1–3 word chunks changing ≈ every 0.5–1 s ⇒ narration roughly **2.7–3.3 words/s (~160–200 wpm)** **[INFERRED, low confidence]**. A 38 s Short ≈ **100–125 words**.
- **Voice [SPEC]**: clear, warm, mildly amused storyteller; consistent single narrator across all videos (brand voice). Slight upward lift on the hook, flatter on facts, slower + lower on the last line (irony).
- **Delivery rules**: speak in complete short sentences; **one breath = one visual**; micro-pause (0.15–0.25 s) before every "But…" / "Then…" / the final fact; hit the key number with stress.
- **Music [SPEC]**: low-volume, light, quirky-playful loop (pizzicato/ukulele/lo-fi). −24 to −28 LUFS under voice at −14 LUFS integrated.
- **SFX [SPEC, mapped to the visuals]**: pop = soft "bloop"; stamp = thud; calendar flip = paper flick; money rain = coin shimmer; star = chime; ❌ = buzzer; VS = whoosh+hit; phone text = ping; hard cuts = optional subtle whoosh only on scene changes that jump location. Keep SFX ≤ −18 dB under voice. Don't SFX every cut.
- **Mix**: voice −14 LUFS, music −26, SFX peak −10 dBFS.

---

## 9. SCRIPTWRITING FORMULA

### 9A. What the evidence shows
**Reconstructed beat sheets** (from caption words and descriptions; approximate timestamps)

**"This King Regretted His Experiment" (41 s)**
| t | Beat | Visual |
|---|---|---|
| 0–1 | HOOK: king offered… | king close-up, robe |
| 2–5 | 2 identical twins on death row; a deal: live | gallows, scroll, hands up |
| 6–11 | The deal: one drinks 3 pots coffee, other 3 tea, for life | copper pots, teapots |
| 12 | Context stamp: "1700s" | carriage street |
| 13–15 | King's belief: coffee is slow poison | thought bubbles ☕→☠️ |
| 16–19 | He banned coffee | "BANNED" woman |
| 20–21 | Deal accepted | scroll, jail |
| 22–24 | Two doctors in charge, Day 1 | calendar |
| 25–26 | "To see who'd die first" | COFFEE VS TEA |
| 27–31 | TWIST: king was shot first; both doctors died | masquerade, pistol, tombstones |
| 32–37 | Tea twin lives on: Age 38 → 64 → 83 | age overlays |
| 38–41 | PAYOFF (irony): the king was already dead | prison yard "dead" |

**"This Woman's Revenge Created Nashville Hot Chicken" (39 s)**
Hook (woman + cayenne) → mini-context: "famous dishes" (Statue of Liberty with chili torch) → why: he stayed out all night → breakfast, chicken to punish → *he loved it* → chicken shack → "70 YEARS" → "KFC put it on menus" → nationwide map → TWIST ENDING: *nobody knows who she was* (the "?" head, crowd of women).

**"Burger King Offered $5,000 To Find This Guy" (40 s)**
Hook (a man says "I'm not Herb") → what that gets you (Whopper 99¢) → who Herb is (made-up character, only man who never ate a Whopper) → $40M ads → Super Bowl reveal → $5,000 for spotting him in every state → payoff: a 16-year-old spotted him.

**"Tesla Regrets Ghosting This Bakery" (50 s)**
Hook-setup (tiny CA bakery, 4,000 mini pies) → text arrives → she buys ingredients, bakes → Tesla cancels by text, won't pay → she posts online → Musk steps in → paid for everything → payoff: Tesla re-orders, she's too busy ("Regrets").

### 9B. The Formula — "THE ODD-STAKES LOOP" [derived]
```
0.0–2.5 s   HOOK        [Entity] + [unexpected verb] + [specific person/number]. ≤14 words.
2.5–8 s     PREMISE     The weird deal/rule/situation in concrete facts (year, place, amount).
8–28 s      ESCALATION  3–5 steps. Each step = 1 sentence = 1 new noun = 1 new visual. Cause → effect.
~60–65 %    TURN        "But when…" / "Then…" / "Until…" — the reversal.
last 6–10 s PAYOFF      The ironic consequence (the "regret") + one final number/fact.
last 2 s    KICKER      Final image holds the irony. No CTA, no recap, hard stop.
```
**Hook formulas (copy the shapes, not the words)** [OBSERVED in titles]
1. *[Giant brand] Regrets [doing something to a small person]* — Nintendo/Tesla.
2. *[Entity] Offered $[amount] To [Find/Do] [odd thing]* — Burger King.
3. *[Entity] Saved/Created/Invented [big thing] by accident/revenge* — Domino's, Nashville.
4. *When [Country] Tried To BAN [common thing]* — Italy/Pasta, Britain/Bread.
5. *This [Role] [Absurd Action]* — "This Sushi Shop Made People Change Their Names".
6. *How [Unexpected Entity] Invented [Familiar Thing]* — North Korea Fast Food.
**Rule:** the title must make the viewer ask *"why/how?"* in <1 s.

**Sentence construction patterns [OBSERVED via caption words]**
- Short declaratives, **8–14 words**, subject-verb-object.
- Time/place anchor early: *"In 2016, a man in Oregon…"*, *"In 1985, Burger King…"*
- Connectors that drive momentum: **But / Then / Until / So / Because / And when.**
- Numbers are stated and shown (4,000; 40 million; 70 years; 83).
- Plain vocabulary, no jargon, no adjectives that don't create an image.
- **One idea per sentence; each sentence changes the picture.**

**Curiosity techniques**
- *Withheld outcome*: say "…and what the police found behind his door" (Domino's) without saying it.
- *Open loop with a number*: "$5,000 to anyone who spotted him".
- *Known-name collision*: giant brand + tiny person.
- *Dramatic irony*: viewer learns the twist (king died first) while the characters didn't.
- *Mystery silhouette ("?")* until the reveal.

**Retention strategy (script level)**
1. Hook inside the first sentence. 2. Never explain background longer than one sentence. 3. Reveal the answer last, but **plant a smaller reveal mid-way** (the "turn"). 4. Each 4–6 s deliver a new fact or reversal. 5. Cut every sentence that doesn't change the picture or the stakes.

**Length math**: 35–45 s ≈ **95–125 words**, **9–12 sentences**, **20–28 scenes**.

**Payoff types seen** (pick one): *Irony* (king died first), *Scale* (70 years → nationwide), *Human consequence* (man found after a stroke), *Legal/economic comeuppance* (Nintendo's lawyers lost; Tesla re-orders too late), *Reveal of identity* (Herb), *Unfinished mystery* (the unnamed woman).

---

## 10. RETENTION & STORYTELLING PRINCIPLES

**Directly observed**
- Protagonist visible and captioned at t=0. No logo bumper, no "hey guys".
- Scene changes ≈ every 1.7 s; some visual event ≥ 1/s.
- Concrete props for every claim (phone, calendar, document) — "show, don't just say".
- Dark topics are softened with cartoon faces/gags.
- Short length (<50 s).

**Hypotheses on why it works [HYPOTHESIS]**
- The face is cartoon, the world is real ⇒ **uncanny-but-memorable thumbnail-in-motion**; the combo is instantly recognisable in the feed.
- Constant picture changes + 1–3-word captions force the eye to keep moving ⇒ low scroll-away.
- The title promises a *twist*; the viewer stays to resolve it.
- The "?" silhouette and the **mid-video turn** create two open loops.
- Replays: a 35-s story with a punchline invites re-watch (watch-time-percent can exceed 100%) — **cannot verify**.

**Topic selection filter** (from the performance tiers):
1. Is there a **person with stakes** (life, justice, revenge, underdog)? (+++)
2. Is there a **famous entity** the viewer already recognises? (++)
3. Is there a **reversal** by the 60% mark? (++)
4. Can every beat be drawn as one picture? (required)
5. Pure promo gimmicks ("1-cent Whoppers") performed weakest on this channel → only choose them if the human angle is strong.

**Accuracy guardrail [important]**: the top video claims North Korea "invented" pizza/hamburgers/burritos, a claim I haven't verified and which reads like folklore/propaganda rather than established history. A viral spike on shaky facts is a trust and policy risk. **Rule: every claim needs ≥2 reliable sources and exact numbers/dates; label legends as legends ("according to state media…").**

---

## 11. COMPLETE VIDEO PRODUCTION WORKFLOW (≈ 90–120 min/Short once templated)

1. **Topic (10 min)** — pass the §10 filter. Source: 2+ reliable articles. Write a *fact sheet* (who/when/where/numbers/outcome).
2. **Title + hook (5 min)** — 5 title variants in the §9 shapes; pick the one that provokes "why?". Add 😯 + topic emoji.
3. **Script (15 min)** — Odd-Stakes Loop, 95–125 words, one idea/sentence. Run it through `SCRIPT_REVIEW_SYSTEM.md`; iterate until every score ≥ 8.
4. **Shot list (15 min)** — table: `#, words, background, character (role+pose+head), prop, overlay, animation, SFX, duration`. Target 20–28 rows; ≥3 inserts; one "wow beat" every ~8–10 s.
5. **Asset prep (30 min)** — generate/cut backgrounds (hue per scene), bodies from Role Library, props, heads (expressions); check licenses.
6. **Voice (10 min)** — record/generate; trim breaths; −14 LUFS.
7. **Assembly (30 min)** — stack template (§3C); cut on first syllable; add captions preset; apply pop-in/idle presets.
8. **Sound (10 min)** — music bed, SFX map.
9. **QC (§12), export** — 1080×1920, 30 fps, H.264, 12–16 Mbps.
10. **Upload** — title, description (2–4 sentences ending "The story of …"), `#food #history #shorts` (adapt tags to topic), publish.

---

## 12. QUALITY-CONTROL CHECKLIST

**Hook**: ☐ Protagonist on screen at 0.0 s ☐ first caption word at frame 0 ☐ hook sentence ≤14 words ☐ title shape + 😯+emoji
**Story**: ☐ Year/place/numbers stated ☐ one idea per sentence ☐ a turn at ~60% ☐ payoff = irony/scale/human consequence ☐ ends on image, no CTA ☐ every fact verified, legends labelled
**Pace**: ☐ avg scene ≤ 2.0 s ☐ something changes every ≤1 s ☐ ≥3 insert shots ☐ no 2 consecutive same backgrounds ☐ 1 wow-beat/8–10 s
**Visual**: ☐ one dominant hue/scene ☐ pre-1990 = B&W world, coloured hero ☐ characters keep the same outfit/head all video ☐ cartoon head matches neck skin tone ☐ soft contact shadows ☐ captions not covering faces/props
**Captions**: ☐ 1–3 words ☐ white + black outline ☐ lower-middle ☐ in sync ☐ bottom UI zone clear
**Audio**: ☐ voice −14 LUFS ☐ music ≥ 10 dB under voice ☐ SFX only on beats ☐ no clipping ☐ pause before "But/Then" and before final line
**Legal**: ☐ asset licenses logged ☐ no logo used as our branding ☐ no impersonation of real people as real/endorsing ☐ no unverified allegation presented as fact

---

## 13. THINGS I'M NOT CERTAIN ABOUT (to confirm)
1. Voice/music/SFX (unheard).
2. Exact caption font and whether keywords get colour highlights.
3. Whether the Shorts loop at the end.
4. Whether heads are animated (mouth flapping) or swapped stills.
5. Which tools produce the images/bodies (AI vs. stock).
6. True average words/second.

*Contact sheets for every video: `reference/contact-sheets/`.*
