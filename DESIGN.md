---
name: Devil Penakut
description: Personal blog as a newspaper morgue: parchment broadsheet, ink, one ember stamp.
colors:
  parchment: "#e2dedb"
  bone: "#cdc6be"
  paper: "#ebe8e5"
  ink: "#1d1d1b"
  charcoal: "#5c5853"
  ember: "#ad3810"
typography:
  display:
    fontFamily: "Bodoni Moda, Didot, serif"
    fontSize: "clamp(4.5rem, 19.5vw, 22rem)"
    fontWeight: 900
    lineHeight: 0.74
    letterSpacing: "-0.06em"
  headline:
    fontFamily: "Bodoni Moda, Didot, serif"
    fontSize: "clamp(2.5rem, 6.4vw, 6rem)"
    fontWeight: 800
    lineHeight: 0.92
    letterSpacing: "-0.045em"
  title:
    fontFamily: "Bodoni Moda, Didot, serif"
    fontSize: "2.1rem"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.025em"
  body:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "1.1875rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "0.75rem"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "0.08em"
  nameplate:
    fontFamily: "Pirata One, serif"
    fontSize: "1.75rem"
    fontWeight: 400
    lineHeight: 1
rounded:
  none: "0px"
  sm: "2.88px"
spacing:
  gutter: "clamp(16px, 4vw, 43px)"
  hair: "7px"
  tight: "14px"
  base: "22px"
  loose: "43px"
  column: "58px"
  section: "65px"
components:
  display-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.parchment}"
    typography: "{typography.display}"
    padding: "clamp(22px, 3vw, 43px) clamp(16px, 4vw, 43px)"
  stub:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: "29px"
  stamp-mark:
    textColor: "{colors.ember}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "2px 6px 1px"
---

# Design System: Devil Penakut

## Overview

**Creative North Star: "The Morgue Broadsheet"**

The blog is a newspaper morgue. Every post is filed under a giant year numeral in a drawer column, newest edition on top. The surface is a printed sheet: parchment stock, ink rules, one ember stamp. Nothing floats, glows, or rounds off. Depth comes from rule weight and the contrast between ink and paper, never from shadow.

Type carries the identity. Bodoni Moda at black weight, crushed to line-height .74 to .92 and tracked tight, sets the banner, headlines and year numerals. Source Serif 4 sets the reading text, which is measured to 68ch and reads like a column. The nameplate alone is set in Pirata One blackletter. The density is archival: a long list, scanned by year, opened to read one piece.

Built from the owner-pinned Miranda broadsheet (see `DESIGN MIRANDA.md`). Where the build diverges from that source, the build wins; the deviations are listed below.

**Key Characteristics:**
- Parchment ground, ink type, one ember accent.
- Oversized Bodoni display, crushed and tracked tight.
- Hairline ink rules instead of boxes, cards, or shadows.
- Year-drawer archive: giant numerals in a sticky left column.
- Stamped marks for state: "Judul saja" on title-only stubs.
- Square images, 0px radius; the only rounded form is the 2.88px stamp.

**Deliberate deviations from the source (recorded, not defects):**
- Charcoal darkened to #5c5853 and ember to #ad3810 for 4.5:1 text on parchment.
- Paper #ebe8e5 is an inset lighter than bone; bone is used only for code backgrounds, so the ember stamp clears 4.5:1 on paper.
- Body is Source Serif 4 at 400, not 300.
- Bodoni Moda stands in for Canopee; it is looser than Canopee's compression.
- Pirata One is used for the nameplate only (masthead and colophon).
- No shadows are built. The source's directional ink shadow on cards is not carried over.

## Colors

Two neutrals carry the page, one ink carries text and rules, and one ember carries the stamp family. The palette is monochrome except for that single stamp accent.

### Primary
- **Ink Black** (#1d1d1b): All text, rules, banner fill, and selection background. The only dark value in the system.
- **Ember Stamp** (#ad3810): The one chromatic accent. Used for the seal, the stamp mark, the focus outline, and the text caret. Never for body text, links, or large fills.

### Secondary
- **Parchment Stock** (#e2dedb): Page ground. Also the text color on ink banners and the seal's perforation.
- **Paper Inset** (#ebe8e5): Filled insets only: the "Judul saja" stub and the seal face.

### Tertiary
- **Bone Cream** (#cdc6be): Code background inside entries and the scrollbar track. Not a surface color.

### Neutral
- **Charcoal Ink** (#5c5853): Secondary text: masthead est., year counts, bylines, captions, post-nav labels.

### Named Rules
**The One Stamp Rule.** Ember appears only in the seal, stamp marks, focus outline, and caret. A screen carries one chromatic note, and its rarity is the point.

## Typography

**Display Font:** Bodoni Moda (fallback Didot, serif). Substitutes Canopee.
**Body Font:** Source Serif 4 (fallback Georgia, serif).
**Nameplate Font:** Pirata One (fallback serif). Masthead and colophon name only.

**Character:** A Didone display crushed into a poster and a readable serif column. The pairing reads as a printed newspaper: loud at the top, quiet in the body.

### Hierarchy
- **Display** (900, clamp(3.5rem, 18vw, 20rem), line-height .74, −0.06em): Full-bleed ink banner title in uppercase, and the year numerals in the archive drawer (line-height .78). Also the post-aside year link.
- **Headline** (800, clamp(2.5rem, 6.4vw, 6rem), line-height .92, −0.045em): Post and page titles; lead story title on home at clamp(2.6rem, 5.6vw, 5.4rem), line-height .9. Long titles drop to clamp(2.2rem, 4.6vw, 4.4rem).
- **Title** (700, 2.1rem / 1.6rem / 1.3rem for h2/h3/h4, line-height 1.05, −0.025em): Headings inside entries.
- **Body** (400, 1.1875rem, line-height 1.6; 1.125rem under 760px): Entry text. Measure capped at 68ch. Lead excerpt capped at 46ch.
- **Label** (500, 0.75rem, line-height 1.2, 0.08em, uppercase): Stamp marks only.

Archive titles sit at 1.25rem, weight 400, line-height 1.3. Bylines and captions sit at 0.875rem in Charcoal Ink.

### Named Rules
**The Crushed Display Rule.** Bodoni display sets at line-height .74 to .92 with negative tracking (−0.04 to −0.06em). Body text never does. Open leading on display type is the bug.

## Layout

No max-width container. Content is set on a gutter of clamp(16px, 4vw, 43px) with rule-to-rule full-width bands. The post and page grid is 4fr / 8fr: a 58px column gap, the sticky year aside in column one, and the entry in column two. Home lead is 7fr / 5fr with a 58px gap. The archive year row is 4fr / 8fr. The year list is auto-fill columns at minmax(15rem, 1fr) with a 36px column gap and 29px row gap.

The vertical rhythm steps through observed values: 7, 14, 22, 29, 36, 43, 58, 65px. Lead and post top padding is 65px and 58px. Year rows are separated by 43px padding.

**Responsive (under 760px):** the masthead drops the "Sejak 2008" est. label. Lead, year, post, and page collapse to one column. The year head becomes an inline row. The post aside is hidden. The seal goes static, 84px wide, above the lead text. Post nav is one column.

## Elevation & Depth

Flat. No `box-shadow` is declared anywhere in the build. Depth is conveyed by ink rules, ink and paper value contrast, and the paper inset on the stub and seal. The source's directional ink shadow is not built; add it only if a card component is introduced, and record it then.

### Named Rules
**The Ruled Not Shadowed Rule.** Structure is drawn with ink rules: 1px for the section and dateline rules, 4px for the colophon top rule, 3px double for entry dividers. The only filled containers are the ink banner, the paper stub, and the paper seal.

## Shapes

Square by default. Images use 0px radius (`img { border-radius: 0 }`). Stub and seal are square-cornered. The one rounded form is the stamp mark at 2.88px, which is rotated −2deg. Borders are 1px ink hairlines. The seal is a rounded-corner rectangle (rx 6 in its SVG) and perforated with a dashed parchment stroke.

## Components

### Display Banner
Full-bleed ink band. Title "Devil / Penakut" in parchment Bodoni black, uppercase, crushed to .74 line-height with a −0.04em negative left margin. Overflow hidden. This is the home opening.

### Masthead
Three-column hairline bar under the top edge: est. label left, nameplate centre, Arsip and Tentang links right. Nameplate in Pirata One at 1.75rem. Links are underlined on hover and when current.

### Dateline Strip
A ruled strip of three spans (count, year range, description) that sits between banner and lead. It is a page-level bar. It is not a per-heading kicker.

### Lead Story
Title in Bodoni at headline size, flanked by a drop-cap excerpt (first letter 5.4em, Bodoni 900, float left). Date below the title. "Baca tulisan ini" is a plain text link.

### Seal
An SVG stamp, 108px wide on desktop, rotated −8deg. Ember sunburst, paper face, Bodoni "2008" and "SEJAK" caps. It stamps in once over .7s and is disabled under reduced motion.

### Year Drawer
Sticky left column with the giant year numeral and count. Right column lists that year's posts as a grid. Each item is a text link with a byline under it. Title-only posts carry a stamp mark inline with their date.

### Stamp Mark
Ember text in a 1px ember border, 2.88px radius, uppercase, −2deg rotation. Used for "Judul saja" only, on title-only stubs and their year-list entries.

### Stub
Paper inset, 29px padding, 68ch max width. Holds the stamp mark and a single explanatory paragraph when a post has no body.

### Post Nav
Two-column ruled band under the entry. Each link is Source Serif 600 at 1.25rem with a small charcoal "Sebelumnya" or "Berikutnya" label above.

### Colophon
Ink top rule (4px). Nameplate and about line on the left, links (Instagram, Twitter, GitHub, Feed) on the right, when configured.

## Do's and Don'ts

### Do:
- **Do** set display type in Bodoni at line-height .74 to .92 with negative tracking.
- **Do** keep images at 0px radius and flush to column edges.
- **Do** draw structure with 1px ink rules, and use the paper inset for a single stub or seal.
- **Do** put dates and bylines below headings.
- **Do** mark title-only posts with the "Judul saja" stamp mark.
- **Do** keep body text at 68ch or less and left-aligned.

### Don't:
- **Don't** set display or body type in a sans-serif or a system display face. The serif and blackletter pairing is the world.
- **Don't** add a second chromatic accent. Ember is the only colour outside the neutrals.
- **Don't** use ember for body text, links, or large fills.
- **Don't** put kickers or eyebrows above headings. Dates and bylines sit below.
- **Don't** introduce gradients, glassmorphism, or blur.
- **Don't** round corners on images or blocks; the 2.88px stamp is the only rounded form.
