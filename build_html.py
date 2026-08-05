# -*- coding: utf-8 -*-
"""Build the English presentation deck: true 16:9 slides with a presentation mode."""
import content as C
import html

def esc(x): return html.escape(str(x))

S = []
def slide(body, cls=""):
    S.append(f'<section class="slide {cls}">{body}</section>')

# ══════════════════════════════ 1. TITLE
slide(f"""
  <div class="t-inner">
    <div class="eyebrow">Cybersecurity Project</div>
    <h1>{esc(C.PROJECT['title_en'])}</h1>
    <div class="rule"></div>
    <p class="t-sub">{esc(C.PROJECT['subtitle_en'])}</p>
    <div class="t-foot">
      <span>{esc(C.PROJECT['author'])}</span><i></i><span>{esc(C.PROJECT['date'])}</span>
    </div>
  </div>""", "title")

# ══════════════════════════════ 2. THE BRIEF
slide("""
  <h3>The project in four points</h3>
  <div class="brief">
    <div class="brief-row">
      <div class="bnum">01</div>
      <div><b>A real virtual lab</b><span>A Proxmox VE node running under nested virtualisation, fully isolated</span></div>
    </div>
    <div class="brief-row">
      <div class="bnum">02</div>
      <div><b>Ten defensive skills executed, not described</b><span>Drawn from a library of 817 skills across 29 domains</span></div>
    </div>
    <div class="brief-row">
      <div class="bnum">03</div>
      <div><b>Executed through an AI agent</b><span>The library is built for this: every skill ships a runnable agent</span></div>
    </div>
    <div class="brief-row hi">
      <div class="bnum">04</div>
      <div><b>Measured, not just applied</b><span>Every control mapped to MITRE ATT&amp;CK and NIST CSF 2.0</span></div>
    </div>
  </div>""")

# ══════════════════════════════ 3. LIBRARY STATS
slide(f"""
  <h3>The source library</h3>
  <div class="stats">
    <div class="stat"><b>817</b><span>skills</span></div>
    <div class="stat"><b>29</b><span>domains</span></div>
    <div class="stat"><b>6</b><span>frameworks</span></div>
    <div class="stat acc"><b>10</b><span>applied here</span></div>
  </div>
  <p class="lead">{esc(C.INTRO['about_repo_en'])}</p>
  <div class="callout warn"><b>The scope is entirely defensive.</b> Everything was carried out inside an isolated lab we own and are authorised to test.</div>""")

# ══════════════════════════════ 4. AI AGENT
slide(f"""
  <h3>How the agent executes a skill</h3>
  <div class="two">
    <div>
      <p class="lead sm">{esc(C.INTRO['agent_method_en'])}</p>
      <div class="callout"><b>The agent executed; the engineering judgement stayed human:</b> which skills to pick, how to design the zones, what to substitute when a tool was unavailable, and how to read the result.</div>
    </div>
    <div class="filetree">
      <div class="ft-h">skill/</div>
      <div class="ft-row"><code>SKILL.md</code><span>YAML frontmatter for discovery + Markdown workflow</span></div>
      <div class="ft-row hi"><code>scripts/agent.py</code><span>The runnable agent that performs the skill</span></div>
      <div class="ft-row"><code>references/</code><span>Technical references</span></div>
      <div class="ft-row"><code>.claude-plugin/</code><span>Registers the library as an agent extension</span></div>
    </div>
  </div>""")

# ══════════════════════════════ 5. DIVIDER
slide("""<div class="d-inner"><span>01</span><h2>Lab Architecture</h2><p>Successive layers of defence on a single node</p></div>""", "divider")

# ══════════════════════════════ 6. ARCHITECTURE
LAYERS = [
    ("Access",     "Tailscale ZTNA + TLS 1.3",        "4 · 5",     "#0E7C86"),
    ("Edge",       "Firewall (default deny) + VLANs", "1 · 2",     "#15616d"),
    ("Monitoring", "Suricata IDS → SIEM correlation", "3 · 6 · 7", "#1d4e6b"),
    ("Hardening",  "Vulnerability scanning + SBOM",   "8 · 10",    "#123a56"),
    ("Deception",  "Ransomware canary files",         "9",         "#0b2a4a"),
]
bars = "".join(
    f'<div class="layer" style="--c:{c}">'
    f'<div class="l-name">{esc(n)}</div>'
    f'<div class="l-comp">{esc(comp)}</div>'
    f'<div class="l-sk">{esc(sk)}</div></div>'
    for n, comp, sk, c in LAYERS)
slide(f"""
  <h3>Five layers, ten skills</h3>
  <div class="arch">{bars}</div>
  <div class="arch-note">If one layer fails, the next one catches it. That is exactly what happened: two Suricata rules never fired, yet the tunnel was still detected through DNS analysis.</div>""")

# ══════════════════════════════ 7. DIVIDER
slide("""<div class="d-inner"><span>02</span><h2>The Ten Skills</h2><p>Chosen to form a connected system, not a list</p></div>""", "divider")

# ══════════════════════════════ 8. SKILLS GRID
cells = "".join(
    f'<div class="sk-card"><div class="sk-n">{s["n"]:02d}</div>'
    f'<div class="sk-t">{esc(s["name_en"])}</div>'
    f'<div class="sk-d">{esc(s["domain"])}</div></div>'
    for s in C.SKILLS)
slide(f"""<h3>Overview</h3><div class="sk-grid">{cells}</div>""")

# ══════════════════════════════ 9-13. SKILL PAIRS
def skill_panel(s):
    steps = "".join(f"<li>{esc(x)}</li>" for x in s["steps_en"][:4])
    att = "".join(f'<span class="tag att">{esc(t)}</span>' for t in s["attack"][:4]) or '<span class="tag att">n/a</span>'
    nist = "".join(f'<span class="tag nist">{esc(t)}</span>' for t in s["nist"][:3])
    return f"""
    <div class="sp">
      <div class="sp-head"><span class="sp-n">{s['n']:02d}</span>
        <div><b>{esc(s['name_en'])}</b><i>{esc(s['domain'])}</i></div></div>
      <p class="sp-what">{esc(s['what_en'])}</p>
      <ol class="sp-steps">{steps}</ol>
      <div class="sp-tags">{att}{nist}</div>
    </div>"""

for i in range(0, 10, 2):
    pair = C.SKILLS[i:i+2]
    slide(f"""<h3>Skills {pair[0]['n']}&ndash;{pair[-1]['n']}</h3>
      <div class="sp-two">{''.join(skill_panel(s) for s in pair)}</div>""")

# ══════════════════════════════ 14. DIVIDER
slide("""<div class="d-inner"><span>03</span><h2>Actual Results</h2><p>Every figure from a real run, with its output kept</p></div>""", "divider")

# ══════════════════════════════ 15. VERIFIED FACTS
rows = "".join(f'<tr><td>{esc(k)}</td><td class="mono">{esc(v)}</td></tr>' for k, v in C.LAB_FACTS)
slide(f"""
  <h3>The lab as it was actually built</h3>
  <table class="facts"><tbody>{rows}</tbody></table>
  <div class="callout">Every row was verified by an actual command on the node, not read off a graphical interface.</div>""")

# ══════════════════════════════ 16. DETECTION CHAIN (hero)
slide("""
  <h3>The complete detection chain</h3>
  <div class="chain">
    <div class="ch"><div class="ch-i">1</div><b>Simulated attack</b><span>ICMP sweep · DNS queries · port scan</span></div>
    <div class="ch-a"></div>
    <div class="ch"><div class="ch-i">2</div><b>Suricata capture</b><span>36 DNS events in the EVE logs</span></div>
    <div class="ch-a"></div>
    <div class="ch"><div class="ch-i">3</div><b>Independent analysis</b><span>An agent that knew nothing of the attack</span></div>
    <div class="ch-a"></div>
    <div class="ch ok"><div class="ch-i">4</div><b>Confirmed detection</b><span>Two tunnels: 72 and 60 characters</span></div>
  </div>
  <div class="callout hero"><b>Why is this the strongest result?</b> Because the tool that detected is not the tool that captured. There is no closed loop proving itself: a real attack, a real capture, and an independent analysis that arrived at a correct detection.</div>""", "hero")

# ══════════════════════════════ 17. SURICATA
slide("""
  <h3>Detection on the network</h3>
  <div class="two">
    <div>
      <div class="kpi"><b>6</b><span>real alerts logged</span></div>
      <table class="mini">
        <tr><td class="mono">T1048.003</td><td>Exfiltration over DNS</td><td class="n">4&times;</td></tr>
        <tr><td class="mono">T1018</td><td>ICMP sweep</td><td class="n">1&times;</td></tr>
        <tr><td class="mono">T1046</td><td>Port scan</td><td class="n">1&times;</td></tr>
      </table>
    </div>
    <div>
      <p class="lead sm">Suricata 7.0.10 with five rules written specifically for the lab, each tied to a MITRE ATT&amp;CK technique, then tested by generating attack traffic.</p>
      <div class="callout warn"><b>Two rules never fired:</b> the C2 rule, because no HTTP server sat on the test path, and the DNS tunnelling rule, because the query did not match the pcre pattern used.</div>
    </div>
  </div>""")

# ══════════════════════════════ 18. SEGMENTATION + FIREWALL
slide("""
  <h3>Isolation and policy enforcement</h3>
  <div class="two">
    <div>
      <div class="zone-h">Three isolated zones</div>
      <div class="zone"><code>vmbr10</code><span>Servers</span><i>10.10.10.0/24</i></div>
      <div class="zone"><code>vmbr20</code><span>Target systems</span><i>10.10.20.0/24</i></div>
      <div class="zone"><code>vmbr30</code><span>Monitoring</span><i>10.10.30.0/24</i></div>
      <div class="verify">vlan_filtering = 1 &check;</div>
    </div>
    <div>
      <div class="zone-h">Firewall policy</div>
      <div class="rule-row deny"><b>DROP</b><span>All inbound by default</span></div>
      <div class="rule-row allow"><b>ALLOW</b><span>Management &rarr; 8006 and 22, logged</span></div>
      <div class="rule-row deny"><b>DROP</b><span>Targets &#8622; management and servers</span></div>
      <div class="verify">verified in iptables &check;</div>
      <p class="foot-note">An automatic rollback was armed before activation, since a default-deny policy can lock out the administrator.</p>
    </div>
  </div>""")

# ══════════════════════════════ 19. SIEM
slide("""
  <h3>Correlation and incident reconstruction</h3>
  <div class="two">
    <div>
      <div class="kpi"><b>26</b><span>events from two sources</span></div>
      <p class="lead sm">Collected from Suricata and the sshd journal, then put through statistics, timeline reconstruction and technique mapping.</p>
    </div>
    <div class="verdict">
      <div class="v-h">ANALYST VERDICT</div>
      <p>A single internal host produced reconnaissance and an exfiltration attempt within <b>twelve seconds</b>.</p>
      <p class="v-c">That tempo points to automated tooling rather than a human operator.</p>
    </div>
  </div>
  <div class="callout"><b>Justified substitution:</b> Splunk Enterprise needs a licensed server, so the same correlation logic was applied to the lab's own real logs.</div>""")

# ══════════════════════════════ 20. REMAINING RESULTS
slide("""
  <h3>Remaining results</h3>
  <div class="res-grid">
    <div class="res"><div class="r-k">TLS 1.3</div>
      <p>The management interface negotiates <span class="mono">TLS_AES_256_GCM_SHA384</span>, with the legacy versions disabled. The certificate is self-signed, which is where the recommendation for a trusted certificate came from.</p></div>
    <div class="res"><div class="r-k">Vulnerability scanning</div>
      <p>Four live hosts, an enumeration of exposed services, and <b>61 packages</b> awaiting updates, ranked in a table by severity.</p></div>
    <div class="res"><div class="r-k">Canary files</div>
      <p><b>16 decoy files</b> with SHA-256 baselines. When encryption was simulated, two alerts fired within milliseconds.</p></div>
    <div class="res"><div class="r-k">SBOM</div>
      <p><b>75 packages</b> checked against the live NVD database. Some results are false positives from name matching, which has to be reviewed in context.</p></div>
  </div>""")

# ══════════════════════════════ 21. COVERAGE
slide("""
  <h3>Measured coverage</h3>
  <p class="lead">This is what makes the title promise measurement: defensive coverage becomes a reviewable figure rather than an impression.</p>
  <div class="cov">
    <div class="cov-col"><div class="cov-h">MITRE ATT&CK</div>
      <div class="cov-tags">
        <span class="tag att">T1046</span><span class="tag att">T1018</span><span class="tag att">T1048.003</span>
        <span class="tag att">T1071.001</span><span class="tag att">T1071.004</span><span class="tag att">T1486</span>
        <span class="tag att">T1557</span><span class="tag att">T1190</span><span class="tag att">T1078</span>
        <span class="tag att">T1133</span><span class="tag att">T1040</span><span class="tag att">T1021</span>
      </div>
      <div class="cov-f">Of these, <b>3 techniques</b> were actually observed in the logs</div>
    </div>
    <div class="cov-col"><div class="cov-h">NIST CSF 2.0</div>
      <div class="cov-tags">
        <span class="tag nist">PR.IR-01</span><span class="tag nist">DE.CM-01</span><span class="tag nist">DE.AE-02</span>
        <span class="tag nist">PR.DS-01</span><span class="tag nist">PR.AA-01</span><span class="tag nist">RS.MA-01</span>
        <span class="tag nist">RS.AN-03</span><span class="tag nist">RC.RP-01</span><span class="tag nist">GV.SC-01</span>
      </div>
      <div class="cov-f">Covering: Protect · Detect · Respond · Recover · Govern</div>
    </div>
  </div>""")

# ══════════════════════════════ 22. WHAT DIDN'T WORK
slide("""
  <h3>What did not work, and how it was handled</h3>
  <div class="fails">
    <div class="fail"><div class="f-t">VLAN setup failed on the first attempt</div>
      <p>A <span class="mono">sed</span> command wrote the directive malformed and the system rejected it. It was rewritten and reapplied until <span class="mono">vlan_filtering = 1</span>.</p></div>
    <div class="fail"><div class="f-t">The firewall failed on the first attempt</div>
      <p>The <span class="mono">+dc/</span> prefix was used, which belongs to IPSets rather than aliases. Corrected, with a rollback armed against lockout.</p></div>
    <div class="fail ok"><div class="f-t">Two rules never fired, yet the tunnel was still found</div>
      <p>Through a different path: subdomain-length analysis. This is precisely what defence in depth means in practice.</p></div>
    <div class="fail"><div class="f-t">Two substitutions and one unfinished step</div>
      <p>Proxmox's firewall instead of pfSense, and a correlation engine instead of licensed Splunk. And <span class="mono">tailscale up</span> requires a personal login, so it was left to the project owner.</p></div>
  </div>""")

# ══════════════════════════════ 23. CLOSING
slide("""
  <div class="t-inner">
    <div class="eyebrow">Conclusion</div>
    <h1 class="close-h">From isolation, to detection, to hardening</h1>
    <div class="rule"></div>
    <p class="t-sub">Ten skills executed on a real node, measured against recognised frameworks,<br>and documented with their raw evidence, including what did not work.</p>
    <div class="t-foot"><span>github.com/OwaisAbuSalah/proxmox-security-lab</span></div>
  </div>""", "title closing")


# ══════════════════════════════ CSS
CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
:root{
 --navy:#0B2A4A; --teal:#0E7C86; --ink:#16202b; --mut:#5f6b7a; --line:#dde5ee;
 --card:#fff; --bg:#e8edf3;
 --att:#8c2233; --attbg:#fdeef0; --nist:#0d5c47; --nistbg:#e7f4ef;
 --warnbg:#fff8ec; --warnb:#d99b1c; --okbg:#e9f5f0; --okb:#0d7a5f;
}
html,body{height:100%}
body{font-family:"Segoe UI",Helvetica,Arial,sans-serif;background:var(--bg);color:var(--ink);
 -webkit-font-smoothing:antialiased;overflow-x:hidden}
.mono,code{font-family:Consolas,"Courier New",monospace}

/* ── deck / slide frame ───────────────────────── */
.deck{padding:26px 14px 90px}
.slide{position:relative;width:min(1160px,96vw);aspect-ratio:16/9;margin:0 auto 26px;
 background:var(--card);border:1px solid var(--line);border-radius:16px;
 padding:52px 60px;overflow:hidden;box-shadow:0 14px 40px rgba(11,42,74,.10);
 display:flex;flex-direction:column;scroll-margin-top:14px}
.slide::after{content:attr(data-n);position:absolute;bottom:20px;right:32px;
 font:600 12px/1 Consolas,monospace;color:#b6c2d0}
.slide::before{content:"";position:absolute;top:0;left:0;width:100%;height:4px;
 background:linear-gradient(90deg,var(--navy),var(--teal))}

h3{font-size:clamp(20px,2.35vw,31px);color:var(--navy);font-weight:700;margin-bottom:22px;
 padding-bottom:13px;border-bottom:2px solid var(--line);position:relative;flex:none}
h3::after{content:"";position:absolute;bottom:-2px;left:0;width:82px;height:2px;background:var(--teal)}
.lead{font-size:clamp(14px,1.3vw,18px);line-height:1.75;color:var(--ink)}
.lead.sm{font-size:clamp(13px,1.16vw,16px);line-height:1.7}
.foot-note{margin-top:12px;font-size:clamp(11px,1vw,13.5px);line-height:1.6;color:var(--mut)}

/* ── title + closing ──────────────────────────── */
.title{background:
   radial-gradient(1100px 520px at 82% -8%,rgba(18,160,173,.30),transparent 62%),
   linear-gradient(155deg,#08223d 0%,#0d3350 52%,#0E7C86 155%);
 border:none;color:#fff;justify-content:center}
.title::before{display:none}
.title::after{color:rgba(255,255,255,.30)}
.t-inner{max-width:88%}
.eyebrow{display:inline-block;font-size:clamp(10px,.9vw,12px);letter-spacing:.30em;text-transform:uppercase;
 color:#8fd7de;border:1px solid rgba(143,215,222,.42);padding:6px 17px;border-radius:999px;margin-bottom:26px}
.title h1{font-size:clamp(24px,3.1vw,45px);line-height:1.28;font-weight:700;color:#fff;letter-spacing:-.01em}
.close-h{font-size:clamp(28px,3.9vw,54px)!important}
.rule{width:104px;height:3px;background:linear-gradient(90deg,#12a0ad,transparent);margin:24px 0 20px;border-radius:2px}
.t-sub{font-size:clamp(13px,1.34vw,19px);color:#cfe1ef;line-height:1.75}
.t-foot{margin-top:38px;display:flex;align-items:center;gap:15px;font-size:clamp(11px,1.05vw,14px);color:#9fbdd2}
.t-foot i{width:5px;height:5px;border-radius:50%;background:#12a0ad;display:inline-block}

/* ── divider ──────────────────────────────────── */
.divider{background:linear-gradient(150deg,#0B2A4A,#123a56 60%,#0E7C86);border:none;color:#fff;justify-content:center}
.divider::before{display:none}
.divider::after{color:rgba(255,255,255,.28)}
.d-inner span{font-size:clamp(52px,7.4vw,104px);font-weight:800;color:rgba(255,255,255,.13);line-height:.86;display:block}
.d-inner h2{font-size:clamp(26px,3.5vw,48px);margin-top:-18px;letter-spacing:-.01em}
.d-inner p{margin-top:14px;font-size:clamp(13px,1.34vw,19px);color:#a9d8de}

/* ── brief ────────────────────────────────────── */
.brief{display:flex;flex-direction:column;gap:13px;flex:1;justify-content:center}
.brief-row{display:flex;gap:20px;align-items:center;background:#f7fafc;border:1px solid var(--line);
 border-radius:13px;padding:17px 22px}
.brief-row.hi{background:linear-gradient(100deg,#0B2A4A,#0E7C86);border:none;color:#fff}
.bnum{flex:none;font:800 clamp(17px,1.75vw,25px)/1 Consolas,monospace;color:var(--teal);width:52px;text-align:center}
.brief-row.hi .bnum{color:#8fd7de}
.brief-row b{display:block;font-size:clamp(14px,1.4vw,20px);color:var(--navy);margin-bottom:4px}
.brief-row.hi b{color:#fff}
.brief-row span{font-size:clamp(12px,1.1vw,15.5px);color:var(--mut);line-height:1.5}
.brief-row.hi span{color:#cfe6ee}

/* ── stats ────────────────────────────────────── */
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:24px}
.stat{background:#f5f9fc;border:1px solid var(--line);border-radius:14px;padding:20px 12px;text-align:center}
.stat b{display:block;font:800 clamp(28px,3.6vw,50px)/1 Consolas,monospace;color:var(--navy)}
.stat span{display:block;margin-top:7px;font-size:clamp(11px,1.05vw,14px);color:var(--mut);text-transform:uppercase;letter-spacing:.08em}
.stat.acc{background:linear-gradient(150deg,#0B2A4A,#0E7C86);border:none}
.stat.acc b,.stat.acc span{color:#fff}

/* ── callouts ─────────────────────────────────── */
.callout{margin-top:auto;background:#f4f9fb;border-left:4px solid var(--teal);
 padding:14px 19px;border-radius:11px;font-size:clamp(12px,1.1vw,15.5px);line-height:1.65}
.callout b{color:var(--navy)}
.callout.warn{background:var(--warnbg);border-left-color:var(--warnb)}
.callout.hero{background:linear-gradient(100deg,#0B2A4A,#0E7C86);border:none;color:#fff;padding:19px 24px}
.callout.hero b{color:#8fd7de}

/* ── two-col ──────────────────────────────────── */
.two{display:grid;grid-template-columns:1fr 1fr;gap:32px;flex:1;align-content:start}
.two>div{display:flex;flex-direction:column}

/* ── file tree ────────────────────────────────── */
.filetree{background:#0f1c28;border-radius:14px;padding:20px 22px;align-self:start}
.ft-h{font:700 clamp(12px,1.1vw,15px)/1 Consolas,monospace;color:#63d9e4;margin-bottom:14px}
.ft-row{display:flex;flex-direction:column;gap:3px;padding:10px 0;border-top:1px solid #1e3243}
.ft-row code{font-size:clamp(11px,1.05vw,14px);color:#d8e6f2}
.ft-row span{font-size:clamp(10.5px,.96vw,13px);color:#8fa6b8;line-height:1.5}
.ft-row.hi code{color:#63d9e4;font-weight:700}

/* ── architecture ─────────────────────────────── */
.arch{display:flex;flex-direction:column;gap:9px;flex:1;justify-content:center}
.layer{display:grid;grid-template-columns:132px 1fr 82px;align-items:center;gap:18px;
 background:var(--c);color:#fff;border-radius:11px;padding:15px 22px}
.l-name{font-weight:700;font-size:clamp(13px,1.28vw,18px);letter-spacing:.01em}
.l-comp{font-size:clamp(11.5px,1.08vw,15px);opacity:.94;font-family:Consolas,monospace}
.l-sk{text-align:center;font:700 clamp(11px,1.05vw,14px)/1 Consolas,monospace;
 background:rgba(255,255,255,.17);padding:5px 9px;border-radius:7px}
.arch-note{margin-top:16px;font-size:clamp(11.5px,1.06vw,15px);color:var(--mut);line-height:1.6;
 border-left:3px solid var(--teal);padding-left:14px}

/* ── skills grid ──────────────────────────────── */
.sk-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:13px;flex:1;align-content:center}
.sk-card{background:#f7fafc;border:1px solid var(--line);border-radius:12px;padding:15px 13px;
 display:flex;flex-direction:column;gap:7px;transition:.15s}
.sk-card:hover{border-color:var(--teal);transform:translateY(-2px)}
.sk-n{font:800 clamp(15px,1.5vw,21px)/1 Consolas,monospace;color:var(--teal)}
.sk-t{font-size:clamp(11px,1.02vw,13.5px);font-weight:600;color:var(--navy);line-height:1.35;flex:1}
.sk-d{font-size:clamp(9.5px,.86vw,11px);color:var(--mut);text-transform:uppercase;letter-spacing:.05em}

/* ── skill pair panels ────────────────────────── */
.sp-two{display:grid;grid-template-columns:1fr 1fr;gap:26px;flex:1}
.sp{background:#f8fafc;border:1px solid var(--line);border-radius:14px;padding:20px 22px;
 display:flex;flex-direction:column}
.sp-head{display:flex;gap:14px;align-items:flex-start;margin-bottom:12px}
.sp-n{flex:none;width:38px;height:38px;border-radius:10px;background:var(--navy);color:#fff;
 display:flex;align-items:center;justify-content:center;font:800 14px/1 Consolas,monospace}
.sp-head b{display:block;font-size:clamp(13px,1.24vw,17px);color:var(--navy);line-height:1.3}
.sp-head i{display:block;font-size:clamp(9.5px,.9vw,11.5px);color:var(--teal);font-style:normal;
 margin-top:4px;text-transform:uppercase;letter-spacing:.06em}
.sp-what{font-size:clamp(11px,1vw,13.5px);line-height:1.62;color:var(--mut);margin-bottom:11px}
.sp-steps{padding-left:19px;margin-bottom:12px;flex:1}
.sp-steps li{font-size:clamp(10.5px,.96vw,13px);line-height:1.5;margin-bottom:5px;color:var(--ink)}
.sp-tags{display:flex;flex-wrap:wrap;gap:5px;margin-top:auto}
.tag{font:700 clamp(9.5px,.88vw,11.5px)/1 Consolas,monospace;padding:4px 8px;border-radius:6px}
.tag.att{background:var(--attbg);color:var(--att)}
.tag.nist{background:var(--nistbg);color:var(--nist)}

/* ── facts table ──────────────────────────────── */
.facts{width:100%;border-collapse:collapse;flex:1;margin-bottom:6px}
.facts td{padding:5px 14px;border-bottom:1px solid var(--line);font-size:clamp(10px,.94vw,12.5px);line-height:1.35}
.facts td:first-child{font-weight:700;color:var(--navy);width:29%}
.facts td:last-child{color:var(--mut)}
.facts tr:nth-child(even) td{background:#f7fafc}

/* ── detection chain ──────────────────────────── */
.chain{display:grid;grid-template-columns:1fr 30px 1fr 30px 1fr 30px 1fr;align-items:stretch;
 margin:6px 0 22px;flex:1;max-height:270px}
.ch{background:#f6fafc;border:1.5px solid var(--line);border-radius:14px;padding:20px 16px;
 display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:9px}
.ch-i{width:38px;height:38px;border-radius:50%;background:var(--navy);color:#fff;
 display:flex;align-items:center;justify-content:center;font:800 16px/1 Consolas,monospace}
.ch b{font-size:clamp(12px,1.16vw,16px);color:var(--navy)}
.ch span{font-size:clamp(10px,.94vw,12.5px);color:var(--mut);line-height:1.45}
.ch.ok{background:linear-gradient(155deg,#0d7a5f,#0E7C86);border-color:transparent}
.ch.ok b,.ch.ok span{color:#fff}
.ch.ok .ch-i{background:rgba(255,255,255,.22)}
/* LTR flow: arrowhead points right */
.ch-a{align-self:center;width:100%;height:2px;background:var(--teal);position:relative}
.ch-a::after{content:"";position:absolute;right:-2px;top:-4px;width:0;height:0;
 border:5px solid transparent;border-left-color:var(--teal)}

/* ── kpi / mini table ─────────────────────────── */
.kpi{background:linear-gradient(150deg,#0B2A4A,#0E7C86);color:#fff;border-radius:14px;
 padding:22px;text-align:center;margin-bottom:16px}
.kpi b{display:block;font:800 clamp(34px,4.2vw,60px)/1 Consolas,monospace}
.kpi span{display:block;margin-top:8px;font-size:clamp(11.5px,1.06vw,15px);color:#cfe6ee;
 text-transform:uppercase;letter-spacing:.07em}
.mini{width:100%;border-collapse:collapse}
.mini td{padding:10px 13px;border-bottom:1px solid var(--line);font-size:clamp(11px,1.03vw,14px)}
.mini td:first-child{font-weight:700;color:var(--att)}
.mini td.n{text-align:right;font-weight:800;color:var(--teal);font-family:Consolas,monospace}

/* ── zones / rules ────────────────────────────── */
.zone-h{font-size:clamp(12px,1.12vw,15.5px);font-weight:700;color:var(--teal);margin-bottom:11px;
 text-transform:uppercase;letter-spacing:.07em}
.zone{display:grid;grid-template-columns:82px 1fr auto;align-items:center;gap:11px;
 background:#f7fafc;border:1px solid var(--line);border-radius:10px;padding:11px 15px;margin-bottom:8px}
.zone code{font-weight:700;color:var(--navy);font-size:clamp(11px,1.02vw,14px)}
.zone span{font-size:clamp(11px,1.02vw,14px)}
.zone i{font-style:normal;font-family:Consolas,monospace;font-size:clamp(10px,.9vw,12px);color:var(--mut)}
.rule-row{display:grid;grid-template-columns:78px 1fr;align-items:center;gap:13px;
 border-radius:10px;padding:11px 15px;margin-bottom:8px;font-size:clamp(11px,1.02vw,14px)}
.rule-row b{font-family:Consolas,monospace;font-size:clamp(10px,.94vw,12.5px);text-align:center;
 padding:4px 7px;border-radius:6px;color:#fff}
.rule-row.deny{background:var(--attbg)} .rule-row.deny b{background:var(--att)}
.rule-row.allow{background:var(--nistbg)} .rule-row.allow b{background:var(--nist)}
.verify{margin-top:10px;font:700 clamp(11px,1.02vw,14px)/1.4 Consolas,monospace;color:var(--okb);
 background:var(--okbg);padding:9px 14px;border-radius:9px;text-align:center}

/* ── verdict ──────────────────────────────────── */
.verdict{background:#0f1c28;color:#d8e6f2;border-radius:14px;padding:24px;align-self:start}
.v-h{font-size:clamp(10.5px,.98vw,13px);letter-spacing:.18em;color:#63d9e4;margin-bottom:14px}
.verdict p{font-size:clamp(13px,1.22vw,17px);line-height:1.65;margin-bottom:11px}
.verdict b{color:#63d9e4}
.v-c{font-size:clamp(11.5px,1.04vw,14px)!important;color:#8fa6b8;border-top:1px solid #1e3243;padding-top:12px}

/* ── results grid ─────────────────────────────── */
.res-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;flex:1;align-content:center}
.res{background:#f7fafc;border:1px solid var(--line);border-radius:13px;padding:18px 21px;
 border-left:4px solid var(--teal)}
.r-k{font-size:clamp(13px,1.22vw,16.5px);font-weight:700;color:var(--navy);margin-bottom:8px}
.res p{font-size:clamp(11px,1vw,13.5px);line-height:1.65;color:var(--mut)}
.res b{color:var(--navy)}

/* ── coverage ─────────────────────────────────── */
.cov{display:grid;grid-template-columns:1fr 1fr;gap:24px;flex:1;align-content:center}
.cov-col{background:#f7fafc;border:1px solid var(--line);border-radius:14px;padding:22px}
.cov-h{font-size:clamp(13px,1.22vw,17px);font-weight:700;color:var(--navy);margin-bottom:15px;
 padding-bottom:10px;border-bottom:2px solid var(--line)}
.cov-tags{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:15px}
.cov-f{font-size:clamp(10.5px,.96vw,13px);color:var(--mut);line-height:1.55;
 border-top:1px solid var(--line);padding-top:12px}
.cov-f b{color:var(--teal)}

/* ── failures ─────────────────────────────────── */
.fails{display:grid;grid-template-columns:1fr 1fr;gap:15px;flex:1;align-content:center}
.fail{background:var(--warnbg);border-left:4px solid var(--warnb);border-radius:12px;padding:17px 20px}
.fail.ok{background:var(--okbg);border-left-color:var(--okb)}
.f-t{font-size:clamp(12.5px,1.16vw,15.5px);font-weight:700;color:var(--navy);margin-bottom:8px}
.fail p{font-size:clamp(11px,1vw,13.5px);line-height:1.65;color:var(--mut)}

/* ── chrome ───────────────────────────────────── */
.bar{position:fixed;top:0;left:0;right:0;z-index:60;background:rgba(232,237,243,.93);
 backdrop-filter:blur(10px);border-bottom:1px solid var(--line);
 display:flex;align-items:center;justify-content:space-between;gap:14px;padding:9px 20px}
.bar .ttl{font-size:13px;font-weight:700;color:var(--navy)}
.bar .ctr{display:flex;align-items:center;gap:9px}
.bar button{border:1px solid var(--line);background:#fff;color:var(--navy);border-radius:8px;
 padding:6px 13px;font:600 12px/1 inherit;cursor:pointer;transition:.14s}
.bar button:hover{background:var(--navy);color:#fff;border-color:var(--navy)}
.counter{font:700 12px/1 Consolas,monospace;color:var(--mut);min-width:52px;text-align:center}
.prog{position:fixed;top:0;left:0;height:3px;z-index:61;
 background:linear-gradient(90deg,var(--navy),var(--teal));width:0;transition:width .22s}
.deck{padding-top:64px}

/* ── presentation mode ────────────────────────── */
body.present{overflow:hidden;background:#050c14}
body.present .bar{display:none}
body.present .deck{padding:0;height:100vh;display:flex;align-items:center;justify-content:center}
body.present .slide{display:none;margin:0;width:min(1600px,98vw);
 max-height:96vh;border-radius:10px;box-shadow:0 30px 90px rgba(0,0,0,.6)}
body.present .slide.on{display:flex}
body.present .prog{background:linear-gradient(90deg,#12a0ad,#63d9e4)}
.exit-hint{display:none;position:fixed;bottom:14px;right:18px;z-index:62;
 color:#5f7183;font:11px/1 Consolas,monospace;letter-spacing:.05em}
body.present .exit-hint{display:block}

@media print{
 .bar,.prog,.exit-hint{display:none}
 body{background:#fff}
 .deck{padding:0}
 .slide{box-shadow:none;border:none;border-radius:0;margin:0;page-break-after:always;
  width:100%;aspect-ratio:16/9}
 @page{size:A4 landscape;margin:0}
}
@media(max-width:760px){
 .slide{aspect-ratio:auto;min-height:auto;padding:26px 22px}
 .two,.sp-two,.res-grid,.cov,.fails{grid-template-columns:1fr;gap:16px}
 .stats{grid-template-columns:repeat(2,1fr)}
 .sk-grid{grid-template-columns:repeat(2,1fr)}
 .chain{grid-template-columns:1fr;max-height:none;gap:9px}
 .ch-a{width:2px;height:20px;justify-self:center}
 .layer{grid-template-columns:1fr;gap:5px;text-align:center}
}
"""

JS = r"""
const slides=[...document.querySelectorAll('.slide')];
slides.forEach((s,i)=>{s.id='s'+i;s.dataset.n=String(i+1).padStart(2,'0')+' / '+slides.length});
const prog=document.querySelector('.prog'), ctr=document.querySelector('.counter');
let cur=0, present=false;

function setCur(i,scroll){
  cur=Math.max(0,Math.min(slides.length-1,i));
  ctr.textContent=(cur+1)+' / '+slides.length;
  prog.style.width=((cur+1)/slides.length*100)+'%';
  if(present){slides.forEach((s,k)=>s.classList.toggle('on',k===cur));}
  else if(scroll){slides[cur].scrollIntoView({behavior:'smooth',block:'start'});}
}
function go(d){setCur(cur+d,true)}

function togglePresent(){
  present=!present;
  document.body.classList.toggle('present',present);
  if(present){ if(document.documentElement.requestFullscreen) document.documentElement.requestFullscreen().catch(()=>{}); }
  else if(document.fullscreenElement){ document.exitFullscreen().catch(()=>{}); }
  setCur(cur,!present);
}
document.addEventListener('fullscreenchange',()=>{
  if(!document.fullscreenElement && present){present=false;document.body.classList.remove('present');setCur(cur,true);}
});

addEventListener('keydown',e=>{
  if(['ArrowRight','ArrowDown','PageDown',' '].includes(e.key)){e.preventDefault();go(1)}
  else if(['ArrowLeft','ArrowUp','PageUp'].includes(e.key)){e.preventDefault();go(-1)}
  else if(e.key==='Home'){e.preventDefault();setCur(0,true)}
  else if(e.key==='End'){e.preventDefault();setCur(slides.length-1,true)}
  else if(e.key==='f'||e.key==='F'||e.key==='p'||e.key==='P'){e.preventDefault();togglePresent()}
  else if(e.key==='Escape'&&present){togglePresent()}
});
document.querySelector('#prev').onclick=()=>go(-1);
document.querySelector('#next').onclick=()=>go(1);
document.querySelector('#pres').onclick=togglePresent;

addEventListener('scroll',()=>{
  if(present)return;
  const y=scrollY+120; let n=0;
  slides.forEach((s,i)=>{if(s.offsetTop<=y)n=i});
  if(n!==cur)setCur(n,false);
},{passive:true});

setCur(0,false);
"""

DOC = f"""<!doctype html>
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(C.PROJECT['title_en'])}</title>
<style>{CSS}</style>
</head>
<body>
<div class="prog"></div>
<div class="bar">
  <span class="ttl">Proxmox Security Lab</span>
  <div class="ctr">
    <button id="prev">&lsaquo; Prev</button>
    <span class="counter">1 / {len(S)}</span>
    <button id="next">Next &rsaquo;</button>
    <button id="pres">Present (F)</button>
  </div>
</div>
<div class="deck">
{chr(10).join(S)}
</div>
<div class="exit-hint">Esc to exit &middot; &larr; &rarr; to navigate</div>
<script>{JS}</script>
</body>
</html>"""

out = r"C:\Users\HP\automation\proxmox-security-lab\Proxmox-Security-Lab-Presentation.html"
open(out, "w", encoding="utf-8").write(DOC)
print("saved", out, f"| {len(S)} slides | {len(DOC)//1024} KB")
