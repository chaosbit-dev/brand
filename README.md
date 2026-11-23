# brand

Visual assets for chaosbit-dev: the chaosbit logos, and the avatars for the org's GitHub Apps,
accounts and teams.

Nothing here is deployed or cloned by automation, so it can hold binaries without
bloating the repos agents clone all day.

## logos/

Copies of the chaosbit marks from the [chaosbit.dev](https://github.com/chaosbit-dev/chaosbit.dev)
site's `public/`. **The site's copies are the ones Vercel serves.** If a mark changes, change it
there and copy it here.

| File | What |
|---|---|
| `chaosbit-logo.gif` | Logo |
| `chaosbit-animated-logo.gif` | Animated logo |
| `favicon.png` | Favicon |
| `og-image-large.png` | Open Graph card |

## apps/

One SVG avatar per GitHub App. The SVGs are the source; PNGs are generated and not committed.

- **Kamino Apps** share a stormy-Kamino background (rain, lightning, waves). Each App has its own
  accent colour so the avatars stay distinct at the 20px GitHub shows them at.
- **Sentinel Apps** use the same layout with a charcoal-and-red night palette, so they read as a
  different family.
- **chaosbit Apps** (org tooling that is neither Kamino nor Sentinel) use the same layout with a
  dark-green palette.
- **WBO Studios Apps** (the `wbo-studios` org, a separate org from chaosbit-dev) use the same
  layout with WBO's own warm-brown palette from its website (`#14100E`, `#3A2E26`, cream `#EFE4D4`):
  a starfield and a ringed planet instead of rain and lightning, and rolling ridges instead of waves.
  WBO is moving to copyright-safe releases (v0.3.0), so keep these icons original: no franchise
  characters or marks.

| App | Avatar | Accent |
|---|---|---|
| kamino-author | Cloning tank growing `</>` | `#10B981` green |
| kamino-watcher | Stilt-city dome with a searchlight eye | `#F59E0B` amber |
| kamino-reader | Open data-book with a lens | `#38BDF8` sky |
| kamino-operator | Kaminoan administrator with a headset | `#A78BFA` violet |
| kamino-actions-runners | Gear-headed clone bot sprinting | `#F43F5E` rose |
| kamino-checks | Clipboard of ticks with a badge | `#A3E635` lime |
| kamino-holonet | Transmitter dish with signal arcs | `#22D3EE` cyan |
| kamino-mothma | Senator in white robes | `#E879F9` fuchsia |
| kamino-registry-read | Image crates under a lens | `#FB923C` orange |
| kamino-shadow | Hooded silhouette, dashed outline | `#94A3B8` slate |
| kamino-verify | DNA helix with an approval seal | `#14B8A6` teal |
| kamino-merge | Tipoca gate with a merge glyph through it; the lintel light goes green only at the merge | `#FDE047` lemon |
| chaosbit-renovate | Build droid with a wrench inside refresh arrows | `#FACC15` yellow |
| chaosbit-vault-writer | Datapad with a stylus (writes to datapad) | `#F97316` orange |
| chaosbit-vault-reader | Jedi holocron under a lens (reads holocron) | `#60A5FA` blue |
| chaosbit-billing | Specimen `$0.00` receipt with a coin (simulated vendor paperwork) | `#4ADE80` money green |
| sentinel-registry-reader | Watchtower with a searchlight and padlock shield | `#EF4444` red |
| wbo-studios-claude | d20 with `</>` on its front face (Claude, WBO's game-dev helper) | `#E0312B` WBO red |

### Adding an App

1. Copy `apps/_template.svg` to `apps/<app-slug>.svg` and replace `#ACCENT` with a colour not
   already in the table.
2. Draw the icon where the template's comment says. Keep it inside the centre circle: GitHub crops
   App logos to a circle in some views.
3. Render and check the contact sheet at 40px and 20px:

   ```sh
   python3 scripts/render.py            # all, or: python3 scripts/render.py <slug>
   open out/sheet.png
   ```

4. Upload `out/<app-slug>.png` in the App's settings: Display information → Upload a logo.
   GitHub has no API for App logos.
5. Add a row to the table above.

## accounts/

Avatars for the org's GitHub user accounts and teams. They use the Kamino palette and the same
template as the Apps, and `render.py` renders them alongside the Apps.

| Account or team | Avatar | Accent |
|---|---|---|
| chaosbit-kamino (user) | Clone trooper helmet with an `@` badge | `#6366F1` indigo |
| kamino-agents (team) | Clone squad of three, marked green, pink and sky | `#F472B6` pink |

Upload `out/<slug>.png` by hand: a user's avatar in that account's Settings → Public profile, a
team's in the org's Teams → the team → Settings → Profile picture.

## social/

One 1280×640 social preview per MCP server repo, shown when a repo link is shared. They share one
frame (dark-green terminal window, `#10B981` accent, an icon ring on the right) so the MCP
servers read as a set; the title, tagline, prompt line and icon change per repo.

| Repo | Icon |
|---|---|
| paperless-mcp | Document whose fields are lifted out under a lens |
| comlink | Envelope broadcasting, with a check seal |
| obsidian-git-mcp | Obsidian shard with a git branch through it |
| homeassistant-mcp | House with a lit bulb and a thermostat dial |

Keep everything that matters inside GitHub's safe zone, x 80–1200 and y 80–560: its repo-card
template asks for a 40pt border, and unfurlers crop the edges.

```sh
python3 scripts/render.py --social      # writes out/social/<repo>.png
```

Upload `out/social/<repo>.png` in the repo's Settings → General → Social preview → Edit →
Upload an image. GitHub has no API for it. Repos have no avatars of their own; only the org does.
