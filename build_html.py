# -*- coding: utf-8 -*-
"""Build the presentation: a walkthrough of the ten skills, each with its workflow."""
import content as C
import html

def esc(x): return html.escape(str(x))

S = []
def slide(body, cls=""):
    S.append(f'<section class="slide {cls}">{body}</section>')

# Per-skill presentation data: short workflow labels, tools, and the lab line.
SKILL_META = {
1:  {"steps": ["Map the security zones", "Define a VLAN per zone", "Tag the uplink as a trunk",
              "Filter traffic between zones", "Harden against VLAN hopping"],
     "tools": ["Linux bridges", "802.1Q", "ifreload"],
     "lab": "Three zones were created on the node: servers, targets and monitoring, each on its own bridge.",
     "why": "If one machine is compromised, the attacker should not be able to walk into the rest of the network."},
2:  {"steps": ["Name each zone with an alias", "Deny all inbound by default",
              "Allow only what is needed", "Log every decision", "Verify in the kernel"],
     "tools": ["pve-firewall", "iptables", "aliases"],
     "lab": "Management may reach the node on two ports; the targets zone may reach nothing.",
     "why": "Segmentation draws the walls. The firewall decides who is allowed through the doors."},
3:  {"steps": ["Install the IDS engine", "Attach it to the interfaces to watch",
              "Write detection rules", "Emit structured JSON logs", "Feed the logs onward"],
     "tools": ["Suricata 7", "EVE JSON", "ATT&CK rules"],
     "lab": "Five rules were written by hand, each tied to a specific attacker technique.",
     "why": "Isolation limits damage, but somebody still has to notice that an attack is happening."},
4:  {"steps": ["Connect an identity provider", "Install the client on each device",
              "Write access rules per identity", "Route the lab subnet through it",
              "Stop exposing services publicly"],
     "tools": ["Tailscale", "WireGuard", "ACLs"],
     "lab": "Installed and running on the node, ready to replace any public exposure of the admin interface.",
     "why": "The admin interface should never sit on the open internet. Reach it through an encrypted identity-aware tunnel instead."},
5:  {"steps": ["Enable TLS 1.3 only", "Pick strong cipher suites", "Manage the certificate",
              "Disable the legacy versions", "Audit what the server actually negotiates"],
     "tools": ["OpenSSL", "testssl.sh", "Python ssl"],
     "lab": "The node's own admin interface was audited to see what it really offers a client.",
     "why": "Encryption in transit is only as good as the version and cipher the server is willing to fall back to."},
6:  {"steps": ["Collect logs from every source", "Normalise them into one format",
              "Correlate events across sources", "Rebuild the incident timeline",
              "Map the pattern to known techniques"],
     "tools": ["SPL / correlation", "Suricata EVE", "syslog"],
     "lab": "Alerts from the IDS were combined with authentication logs to reconstruct one story.",
     "why": "A single alert says something happened. Correlated alerts say what happened, in what order, and by whom."},
7:  {"steps": ["Collect DNS query logs", "Measure name randomness (entropy)",
              "Flag unusually long subdomains", "Watch query volume and timing",
              "Raise an alert and attribute the source"],
     "tools": ["entropy analysis", "Suricata DNS", "Python"],
     "lab": "Real captured DNS events were analysed and the hidden tunnel was identified from name length alone.",
     "why": "Almost every network allows DNS out, so attackers hide stolen data inside domain names."},
8:  {"steps": ["Inventory what you actually own", "Scan on a recurring schedule",
              "Rank findings by real risk", "Track remediation to closure", "Re-scan to confirm the fix"],
     "tools": ["nmap", "OpenVAS", "CVSS"],
     "lab": "Lab assets were enumerated and the exposed services on the node were listed and ranked.",
     "why": "You cannot patch what you have not found, and not every finding deserves the same urgency."},
9:  {"steps": ["Place decoy files in sensitive folders", "Record a baseline hash for each",
              "Watch the filesystem in real time", "Classify any interaction",
              "Alert before encryption completes"],
     "tools": ["Python watchdog", "SHA-256", "syslog"],
     "lab": "Decoys were deployed and simulated encryption triggered an alert almost instantly.",
     "why": "No legitimate user opens a file called Passwords.xlsx, so any touch is a signal, not noise."},
10: {"steps": ["Generate an SBOM for the software", "Parse the component list",
              "Match components against the CVE database", "Trace transitive dependencies",
              "Review results in context"],
     "tools": ["syft", "grype", "CycloneDX", "NVD"],
     "lab": "A real dependency list was produced and checked against the live vulnerability database.",
     "why": "Most of your code is somebody else's code. When a library breaks, you need to know immediately whether you shipped it."},
}

# ══════════════════════════════ 1. TITLE
slide(f"""
  <div class="t-inner">
    <div class="eyebrow">Network &amp; Information Security</div>
    <h1>Ten Defensive Security Skills</h1>
    <div class="rule"></div>
    <h2 class="sub2">Built and demonstrated on a Proxmox VE lab</h2>
    <p class="t-sub">What each skill is, how its workflow runs, and where it fits in the defence</p>
    <div class="t-foot"><span>{esc(C.PROJECT['author'])}</span><i></i><span>{esc(C.PROJECT['date'])}</span></div>
  </div>""", "title")

# ══════════════════════════════ 2. WHAT THIS IS
slide("""
  <h3>What this project is</h3>
  <div class="brief">
    <div class="brief-row">
      <div class="bnum">01</div>
      <div><b>A lab to practise defence in</b><span>An isolated Proxmox VE node where controls can be applied, attacked, and observed without touching a real network</span></div>
    </div>
    <div class="brief-row">
      <div class="bnum">02</div>
      <div><b>Ten defensive skills, carried out</b><span>Taken from an open library of security skills, chosen so that each one supports the next</span></div>
    </div>
    <div class="brief-row hi">
      <div class="bnum">03</div>
      <div><b>Each skill has a workflow</b><span>Not a definition to memorise, but an ordered set of steps you follow to put the control in place</span></div>
    </div>
  </div>
  <div class="callout">The rest of this presentation walks through those ten workflows, one slide at a time.</div>""")

# ══════════════════════════════ 3. AI AGENT (kept simple)
slide("""
  <h3>How the skills were carried out</h3>
  <div class="two">
    <div>
      <p class="lead">Each skill in the library is written to be executed, not only read. It ships two things: a description that explains the workflow, and a small program that performs it.</p>
      <p class="lead" style="margin-top:12px">An AI agent reads the description to understand the steps, runs the program, then reads the output and decides what to do next.</p>
      <div class="callout" style="margin-top:16px">Choosing the skills, designing the zones and judging the results stayed a human decision.</div>
    </div>
    <div class="filetree">
      <div class="ft-h">one skill folder</div>
      <div class="ft-row"><code>SKILL.md</code><span>What the skill is and the steps it follows</span></div>
      <div class="ft-row hi"><code>scripts/agent.py</code><span>A runnable program that performs those steps</span></div>
      <div class="ft-row"><code>references/</code><span>Background material</span></div>
    </div>
  </div>""")

# ══════════════════════════════ 4. PROJECT WORKFLOW
slide("""
  <h3>The project workflow</h3>
  <p class="lead sm">The same loop was repeated for every one of the ten skills.</p>
  <div class="pflow">
    <div class="pf"><div class="pf-n">1</div><b>Choose the skill</b><span>Pick the control the lab needs next</span></div>
    <div class="pf"><div class="pf-n">2</div><b>Read the workflow</b><span>Understand the ordered steps it prescribes</span></div>
    <div class="pf"><div class="pf-n">3</div><b>Prepare the lab</b><span>Create the zone, host or service it acts on</span></div>
    <div class="pf"><div class="pf-n">4</div><b>Run the agent</b><span>Execute the skill against the lab</span></div>
    <div class="pf"><div class="pf-n">5</div><b>Verify</b><span>Confirm the control is live, not just configured</span></div>
    <div class="pf"><div class="pf-n">6</div><b>Record it</b><span>Keep the output as evidence</span></div>
  </div>
  <div class="callout"><b>Step 5 is the one that matters.</b> A setting can be written and still not be in effect, so each control was checked where it actually runs.</div>""")

# ══════════════════════════════ 5. DIVIDER
slide("""<div class="d-inner"><span>01</span><h2>The Ten Skills</h2><p>One workflow at a time</p></div>""", "divider")

# ══════════════════════════════ 6-15. ONE SLIDE PER SKILL
for s in C.SKILLS:
    m = SKILL_META[s["n"]]
    steps = "".join(
        f'<div class="wf"><div class="wf-n">{i}</div><div class="wf-t">{esc(t)}</div></div>'
        for i, t in enumerate(m["steps"], 1))
    tools = "".join(f'<span class="chip">{esc(t)}</span>' for t in m["tools"])
    slide(f"""
  <div class="sk-head">
    <span class="sk-big">{s['n']:02d}</span>
    <div><h3 class="sk-h">{esc(s['name_en'])}</h3><div class="sk-dom">{esc(s['domain'])}</div></div>
  </div>
  <div class="sk-body">
    <div class="wf-col">
      <div class="col-lbl">Workflow</div>
      {steps}
    </div>
    <div class="side-col">
      <div class="col-lbl">Why it matters</div>
      <p class="why">{esc(m['why'])}</p>
      <div class="col-lbl">In the lab</div>
      <p class="inlab">{esc(m['lab'])}</p>
      <div class="col-lbl">Tools</div>
      <div class="chips">{tools}</div>
    </div>
  </div>""", "skill")

# ══════════════════════════════ 16. HOW THEY CONNECT
slide("""
  <h3>How the ten fit together</h3>
  <p class="lead sm">They were not picked as a list. Each one hands something to the next.</p>
  <div class="conn">
    <div class="cn"><div class="cn-h">Keep them apart</div><div class="cn-s">01 &middot; 02</div>
      <p>Zones divide the network, and the firewall polices the boundaries between them.</p></div>
    <div class="cn-a"></div>
    <div class="cn"><div class="cn-h">Notice the attack</div><div class="cn-s">03 &middot; 06 &middot; 07</div>
      <p>An IDS watches the traffic, its logs feed correlation, and DNS analysis catches what hides in plain sight.</p></div>
    <div class="cn-a"></div>
    <div class="cn"><div class="cn-h">Reduce the openings</div><div class="cn-s">05 &middot; 08 &middot; 10</div>
      <p>Encrypt the admin path, find exposed services, and know which libraries you depend on.</p></div>
    <div class="cn-a"></div>
    <div class="cn ok"><div class="cn-h">Catch what slips</div><div class="cn-s">04 &middot; 09</div>
      <p>Identity-aware access closes the front door, and decoy files raise the alarm if someone is already inside.</p></div>
  </div>""")

# ══════════════════════════════ 17. THE CHAIN IN ACTION
slide("""
  <h3>The workflows running together</h3>
  <p class="lead sm">To show the skills are not independent exercises, one scenario was run end to end through them.</p>
  <div class="chain">
    <div class="ch"><div class="ch-i">1</div><b>A host in the targets zone</b><span>separated by skills 01 and 02</span></div>
    <div class="ch-a"></div>
    <div class="ch"><div class="ch-i">2</div><b>It behaves suspiciously</b><span>scanning and odd DNS lookups</span></div>
    <div class="ch-a"></div>
    <div class="ch"><div class="ch-i">3</div><b>The IDS records it</b><span>skill 03 watching that zone</span></div>
    <div class="ch-a"></div>
    <div class="ch ok"><div class="ch-i">4</div><b>Analysis names it</b><span>skill 07 identifies the hidden tunnel</span></div>
  </div>
  <div class="callout hero">The host could not reach the management network at all, because the walls from skills 01 and 02 held. What it did do was seen, and what it hid was found.</div>""", "hero")

# ══════════════════════════════ 18. CLOSING
slide("""
  <div class="t-inner">
    <div class="eyebrow">In closing</div>
    <h1 class="close-h">Ten workflows, one defence</h1>
    <div class="rule"></div>
    <p class="t-sub">Separate the network, watch it, harden it, and leave something behind<br>to catch whatever still gets through.</p>
    <div class="t-foot"><span>Thank you</span></div>
  </div>""", "title closing")


# ══════════════════════════════ CSS
CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
:root{
 --navy:#0B2A4A; --teal:#0E7C86; --ink:#16202b; --mut:#5f6b7a; --line:#dde5ee;
 --card:#fff; --bg:#e8edf3; --okb:#0d7a5f; --okbg:#e9f5f0;
}
html,body{height:100%}
body{font-family:"Segoe UI",Helvetica,Arial,sans-serif;background:var(--bg);color:var(--ink);
 -webkit-font-smoothing:antialiased;overflow-x:hidden}
code,.mono{font-family:Consolas,"Courier New",monospace}

.deck{padding:26px 14px 90px;padding-top:64px}
.slide{position:relative;width:min(1160px,96vw);aspect-ratio:16/9;margin:0 auto 26px;
 background:var(--card);border:1px solid var(--line);border-radius:16px;
 padding:48px 56px;overflow:hidden;box-shadow:0 14px 40px rgba(11,42,74,.10);
 display:flex;flex-direction:column;scroll-margin-top:14px}
.slide::after{content:attr(data-n);position:absolute;bottom:18px;right:30px;
 font:600 12px/1 Consolas,monospace;color:#b6c2d0}
.slide::before{content:"";position:absolute;top:0;left:0;width:100%;height:4px;
 background:linear-gradient(90deg,var(--navy),var(--teal))}

h3{font-size:clamp(20px,2.3vw,30px);color:var(--navy);font-weight:700;margin-bottom:18px;
 padding-bottom:12px;border-bottom:2px solid var(--line);position:relative;flex:none}
h3::after{content:"";position:absolute;bottom:-2px;left:0;width:78px;height:2px;background:var(--teal)}
.lead{font-size:clamp(14px,1.3vw,18px);line-height:1.72;color:var(--ink)}
.lead.sm{font-size:clamp(12.5px,1.14vw,16px);line-height:1.62;color:var(--mut);margin-bottom:4px}

/* title */
.title{background:radial-gradient(1100px 520px at 82% -8%,rgba(18,160,173,.30),transparent 62%),
 linear-gradient(155deg,#08223d 0%,#0d3350 52%,#0E7C86 155%);border:none;color:#fff;justify-content:center}
.title::before{display:none}.title::after{color:rgba(255,255,255,.30)}
.t-inner{max-width:88%}
.eyebrow{display:inline-block;font-size:clamp(10px,.9vw,12px);letter-spacing:.30em;text-transform:uppercase;
 color:#8fd7de;border:1px solid rgba(143,215,222,.42);padding:6px 17px;border-radius:999px;margin-bottom:24px}
.title h1{font-size:clamp(30px,4.2vw,58px);line-height:1.2;font-weight:700;color:#fff;letter-spacing:-.015em}
.close-h{font-size:clamp(30px,4.2vw,58px)!important}
.rule{width:104px;height:3px;background:linear-gradient(90deg,#12a0ad,transparent);margin:22px 0 18px;border-radius:2px}
.sub2{font-size:clamp(15px,1.6vw,23px);font-weight:500;color:#a9c9dc}
.t-sub{margin-top:14px;font-size:clamp(13px,1.3vw,18px);color:#cfe1ef;line-height:1.7}
.t-foot{margin-top:34px;display:flex;align-items:center;gap:15px;font-size:clamp(11px,1.05vw,14px);color:#9fbdd2}
.t-foot i{width:5px;height:5px;border-radius:50%;background:#12a0ad;display:inline-block}

/* divider */
.divider{background:linear-gradient(150deg,#0B2A4A,#123a56 60%,#0E7C86);border:none;color:#fff;justify-content:center}
.divider::before{display:none}.divider::after{color:rgba(255,255,255,.28)}
.d-inner span{font-size:clamp(52px,7.4vw,104px);font-weight:800;color:rgba(255,255,255,.13);line-height:.86;display:block}
.d-inner h2{font-size:clamp(28px,3.7vw,50px);margin-top:-18px}
.d-inner p{margin-top:12px;font-size:clamp(13px,1.34vw,19px);color:#a9d8de}

/* brief rows */
.brief{display:flex;flex-direction:column;gap:14px;flex:1;justify-content:center}
.brief-row{display:flex;gap:20px;align-items:center;background:#f7fafc;border:1px solid var(--line);
 border-radius:13px;padding:18px 22px}
.brief-row.hi{background:linear-gradient(100deg,#0B2A4A,#0E7C86);border:none;color:#fff}
.bnum{flex:none;font:800 clamp(17px,1.75vw,25px)/1 Consolas,monospace;color:var(--teal);width:50px;text-align:center}
.brief-row.hi .bnum{color:#8fd7de}
.brief-row b{display:block;font-size:clamp(14px,1.42vw,20px);color:var(--navy);margin-bottom:5px}
.brief-row.hi b{color:#fff}
.brief-row span{font-size:clamp(12px,1.1vw,15px);color:var(--mut);line-height:1.55}
.brief-row.hi span{color:#cfe6ee}

.callout{margin-top:auto;background:#f4f9fb;border-left:4px solid var(--teal);
 padding:14px 19px;border-radius:11px;font-size:clamp(12px,1.1vw,15.5px);line-height:1.62}
.callout b{color:var(--navy)}
.callout.hero{background:linear-gradient(100deg,#0B2A4A,#0E7C86);border:none;color:#fff;padding:18px 24px}
.callout.hero b{color:#8fd7de}

.two{display:grid;grid-template-columns:1.15fr .85fr;gap:34px;flex:1;align-content:start}
.two>div{display:flex;flex-direction:column}
.filetree{background:#0f1c28;border-radius:14px;padding:20px 22px;align-self:start}
.ft-h{font:700 clamp(12px,1.1vw,15px)/1 Consolas,monospace;color:#63d9e4;margin-bottom:14px}
.ft-row{display:flex;flex-direction:column;gap:3px;padding:11px 0;border-top:1px solid #1e3243}
.ft-row code{font-size:clamp(11px,1.05vw,14px);color:#d8e6f2}
.ft-row span{font-size:clamp(10.5px,.96vw,13px);color:#8fa6b8;line-height:1.5}
.ft-row.hi code{color:#63d9e4;font-weight:700}

/* project workflow */
.pflow{display:grid;grid-template-columns:repeat(6,1fr);gap:10px;flex:1;align-content:center;max-height:290px}
.pf{background:#f6fafc;border:1.5px solid var(--line);border-radius:13px;padding:18px 12px;
 display:flex;flex-direction:column;align-items:center;text-align:center;gap:8px;position:relative}
.pf-n{width:34px;height:34px;border-radius:50%;background:var(--navy);color:#fff;
 display:flex;align-items:center;justify-content:center;font:800 15px/1 Consolas,monospace}
.pf b{font-size:clamp(11.5px,1.08vw,15px);color:var(--navy);line-height:1.3}
.pf span{font-size:clamp(9.5px,.9vw,12px);color:var(--mut);line-height:1.45}
.pf:not(:last-child)::after{content:"";position:absolute;right:-7px;top:34px;width:9px;height:2px;background:var(--teal)}

/* skill slides */
.skill{padding:42px 52px}
.sk-head{display:flex;align-items:center;gap:20px;padding-bottom:16px;margin-bottom:20px;
 border-bottom:2px solid var(--line);position:relative;flex:none}
.sk-head::after{content:"";position:absolute;bottom:-2px;left:0;width:78px;height:2px;background:var(--teal)}
.sk-big{font:800 clamp(34px,4.2vw,58px)/1 Consolas,monospace;color:var(--teal);opacity:.85}
.sk-h{font-size:clamp(19px,2.15vw,29px);color:var(--navy);border:none;margin:0;padding:0}
.sk-h::after{display:none}
.sk-dom{font-size:clamp(10.5px,1vw,13px);color:var(--mut);text-transform:uppercase;letter-spacing:.1em;margin-top:5px}
.sk-body{display:grid;grid-template-columns:1.25fr 1fr;gap:40px;flex:1;align-content:stretch}
.col-lbl{font-size:clamp(10.5px,1vw,13px);font-weight:800;letter-spacing:.13em;text-transform:uppercase;
 color:var(--teal);margin-bottom:14px}
.side-col{display:flex;flex-direction:column}
.side-col .col-lbl:not(:first-child){margin-top:22px}

.wf-col{position:relative;display:flex;flex-direction:column}
.wf{display:flex;gap:17px;align-items:flex-start;position:relative;flex:1;padding-bottom:6px}
.wf:not(:last-child)::before{content:"";position:absolute;left:17px;top:38px;bottom:0;width:2px;background:var(--line)}
.wf-n{flex:none;width:35px;height:35px;border-radius:50%;background:var(--navy);color:#fff;z-index:1;
 display:flex;align-items:center;justify-content:center;font:800 14.5px/1 Consolas,monospace}
.wf-t{font-size:clamp(14px,1.42vw,20px);line-height:1.35;color:var(--ink);padding-top:7px}

.why{font-size:clamp(12.5px,1.2vw,16.5px);line-height:1.6;color:var(--ink)}
.inlab{font-size:clamp(12.5px,1.2vw,16.5px);line-height:1.6;color:var(--mut);
 border-left:3px solid var(--teal);padding-left:14px}
.chips{display:flex;flex-wrap:wrap;gap:7px;margin-top:auto;padding-top:8px}
.chip{font:600 clamp(11px,1.04vw,14px)/1 Consolas,monospace;background:#eef4f8;color:var(--navy);
 padding:8px 13px;border-radius:8px;border:1px solid var(--line)}

/* connections */
.conn{display:grid;grid-template-columns:1fr 26px 1fr 26px 1fr 26px 1fr;align-items:stretch;flex:1;max-height:300px}
.cn{background:#f6fafc;border:1.5px solid var(--line);border-radius:14px;padding:18px 15px;
 display:flex;flex-direction:column;gap:7px}
.cn-h{font-size:clamp(12.5px,1.18vw,16.5px);font-weight:700;color:var(--navy);line-height:1.3}
.cn-s{font:700 clamp(10px,.94vw,12.5px)/1 Consolas,monospace;color:var(--teal)}
.cn p{font-size:clamp(10.5px,.98vw,13px);line-height:1.5;color:var(--mut)}
.cn.ok{background:linear-gradient(155deg,#0d7a5f,#0E7C86);border-color:transparent}
.cn.ok .cn-h,.cn.ok p{color:#fff}.cn.ok .cn-s{color:#a9e8ee}
.cn-a{align-self:center;width:100%;height:2px;background:var(--teal);position:relative}
.cn-a::after{content:"";position:absolute;right:-2px;top:-4px;border:5px solid transparent;border-left-color:var(--teal)}

/* chain */
.chain{display:grid;grid-template-columns:1fr 28px 1fr 28px 1fr 28px 1fr;align-items:stretch;
 margin:10px 0 18px;flex:1;max-height:250px}
.ch{background:#f6fafc;border:1.5px solid var(--line);border-radius:14px;padding:20px 15px;
 display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:9px}
.ch-i{width:36px;height:36px;border-radius:50%;background:var(--navy);color:#fff;
 display:flex;align-items:center;justify-content:center;font:800 15px/1 Consolas,monospace}
.ch b{font-size:clamp(12px,1.14vw,16px);color:var(--navy);line-height:1.3}
.ch span{font-size:clamp(10px,.94vw,12.5px);color:var(--mut);line-height:1.45}
.ch.ok{background:linear-gradient(155deg,#0d7a5f,#0E7C86);border-color:transparent}
.ch.ok b,.ch.ok span{color:#fff}.ch.ok .ch-i{background:rgba(255,255,255,.22)}
.ch-a{align-self:center;width:100%;height:2px;background:var(--teal);position:relative}
.ch-a::after{content:"";position:absolute;right:-2px;top:-4px;border:5px solid transparent;border-left-color:var(--teal)}

/* chrome */
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

body.present{overflow:hidden;background:#050c14}
body.present .bar{display:none}
body.present .deck{padding:0;height:100vh;display:flex;align-items:center;justify-content:center}
body.present .slide{display:none;margin:0;width:min(1600px,98vw);max-height:96vh;
 border-radius:10px;box-shadow:0 30px 90px rgba(0,0,0,.6)}
body.present .slide.on{display:flex}
.exit-hint{display:none;position:fixed;bottom:14px;right:18px;z-index:62;color:#5f7183;
 font:11px/1 Consolas,monospace;letter-spacing:.05em}
body.present .exit-hint{display:block}

@media print{
 .bar,.prog,.exit-hint{display:none}
 body{background:#fff}.deck{padding:0}
 .slide{box-shadow:none;border:none;border-radius:0;margin:0;page-break-after:always;width:100%;aspect-ratio:16/9}
 @page{size:A4 landscape;margin:0}
}
@media(max-width:760px){
 .slide{aspect-ratio:auto;min-height:auto;padding:26px 22px}
 .two,.sk-body{grid-template-columns:1fr;gap:20px}
 .pflow{grid-template-columns:repeat(2,1fr);max-height:none}
 .pf:not(:last-child)::after{display:none}
 .conn,.chain{grid-template-columns:1fr;max-height:none;gap:9px}
 .cn-a,.ch-a{width:2px;height:18px;justify-self:center}
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
  if(present){if(document.documentElement.requestFullscreen)document.documentElement.requestFullscreen().catch(()=>{});}
  else if(document.fullscreenElement){document.exitFullscreen().catch(()=>{});}
  setCur(cur,!present);
}
document.addEventListener('fullscreenchange',()=>{
  if(!document.fullscreenElement&&present){present=false;document.body.classList.remove('present');setCur(cur,true);}
});
addEventListener('keydown',e=>{
  if(['ArrowRight','ArrowDown','PageDown',' '].includes(e.key)){e.preventDefault();go(1)}
  else if(['ArrowLeft','ArrowUp','PageUp'].includes(e.key)){e.preventDefault();go(-1)}
  else if(e.key==='Home'){e.preventDefault();setCur(0,true)}
  else if(e.key==='End'){e.preventDefault();setCur(slides.length-1,true)}
  else if('fFpP'.includes(e.key)){e.preventDefault();togglePresent()}
  else if(e.key==='Escape'&&present){togglePresent()}
});
document.querySelector('#prev').onclick=()=>go(-1);
document.querySelector('#next').onclick=()=>go(1);
document.querySelector('#pres').onclick=togglePresent;
addEventListener('scroll',()=>{if(present)return;const y=scrollY+120;let n=0;
 slides.forEach((s,i)=>{if(s.offsetTop<=y)n=i});if(n!==cur)setCur(n,false)},{passive:true});
setCur(0,false);
"""

DOC = f"""<!doctype html>
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ten Defensive Security Skills</title>
<style>{CSS}</style>
</head>
<body>
<div class="prog"></div>
<div class="bar">
  <span class="ttl">Ten Defensive Security Skills</span>
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
