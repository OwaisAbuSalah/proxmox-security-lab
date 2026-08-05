# -*- coding: utf-8 -*-
"""Build the bilingual HTML slide-deck presentation from content.py."""
import content as C
import html

def esc(x): return html.escape(x)

slides = []

# --- Title slide ---
slides.append(f"""
<section class="slide title">
  <div class="badge">Anthropic Cybersecurity Skills · 817 skills · 29 domains</div>
  <h1 dir="rtl">{esc(C.PROJECT['title_ar'])}</h1>
  <h2>{esc(C.PROJECT['title_en'])}</h2>
  <p class="sub" dir="rtl">{esc(C.PROJECT['subtitle_ar'])}</p>
  <p class="sub en">{esc(C.PROJECT['subtitle_en'])}</p>
  <div class="meta">{esc(C.PROJECT['author'])} &nbsp;·&nbsp; {esc(C.PROJECT['date'])}<br>
  <a href="{esc(C.PROJECT['repo'])}">{esc(C.PROJECT['repo'])}</a></div>
</section>""")

# --- Agenda / intro ---
slides.append(f"""
<section class="slide">
  <span class="kicker">01 · Introduction</span>
  <h3 dir="rtl">المقدمة والنطاق <span class="en">/ Introduction &amp; Scope</span></h3>
  <p dir="rtl">{esc(C.INTRO['about_repo_ar'])}</p>
  <p class="en">{esc(C.INTRO['about_repo_en'])}</p>
  <div class="statrow">
    <div class="stat"><b>817</b><span>Skills</span></div>
    <div class="stat"><b>29</b><span>Domains</span></div>
    <div class="stat"><b>6</b><span>Frameworks</span></div>
    <div class="stat"><b>10</b><span>Applied here</span></div>
  </div>
  <p class="note" dir="rtl"><b>النطاق دفاعي (blue-team):</b> {esc(C.INTRO['scope_ar'])}</p>
</section>""")

# --- AI Agent methodology ---
struct = [
    ("SKILL.md","ترويسة YAML + خطوات Markdown","YAML frontmatter + Markdown workflow"),
    ("scripts/agent.py","الوكيل القابل للتشغيل","The runnable agent"),
    ("references/","مراجع تقنية","Technical references"),
    (".claude-plugin/","يسجّل الريبو كإضافة Claude Code","Registers repo as a Claude Code plugin"),
]
srows = "".join(f"<tr><td class='mono'>{esc(f)}</td><td dir='rtl'>{esc(a)}<span class='en'> {esc(e)}</span></td></tr>" for f,a,e in struct)
slides.append(f"""
<section class="slide">
  <span class="kicker">02 · AI Agent Method</span>
  <h3 dir="rtl">التنفيذ عبر وكيل ذكاء اصطناعي <span class="en">/ AI-Agent Execution</span></h3>
  <p dir="rtl">{esc(C.INTRO['agent_method_ar'])}</p>
  <p class="en">{esc(C.INTRO['agent_method_en'])}</p>
  <table class="arch"><thead><tr><th>File</th><th>Purpose</th></tr></thead><tbody>{srows}</tbody></table>
  <p class="note" dir="rtl">{esc(C.INTRO['tiers_ar'])}</p>
</section>""")

# --- Why Proxmox / Architecture ---
arch = [
    ("Access","Tailscale + TLS 1.3 reverse proxy","4 · 5"),
    ("Edge","pfSense firewall + VLAN segmentation","1 · 2"),
    ("Monitoring","Suricata IDS → Splunk / Wazuh SIEM","3 · 6 · 7"),
    ("Hardening","OpenVAS scans + SBOM analysis","8 · 10"),
    ("Deception","Ransomware canary files","9"),
]
rows = "".join(f"<tr><td class='lay'>{esc(l)}</td><td>{esc(c)}</td><td class='sk'>{esc(s)}</td></tr>" for l,c,s in arch)
slides.append(f"""
<section class="slide">
  <span class="kicker">02 · Architecture</span>
  <h3 dir="rtl">معمارية المختبر <span class="en">/ Lab Architecture on Proxmox</span></h3>
  <p dir="rtl">{esc(C.INTRO['why_proxmox_ar'])}</p>
  <table class="arch"><thead><tr><th>Layer</th><th>Component</th><th>Skill</th></tr></thead><tbody>{rows}</tbody></table>
</section>""")

# --- One slide per skill ---
for s in C.SKILLS:
    steps = "".join(f"<li><span class='ar' dir='rtl'>{esc(a)}</span><span class='en'>{esc(e)}</span></li>"
                    for a,e in zip(s['steps_ar'], s['steps_en']))
    attack = " ".join(f"<span class='tag att'>{esc(t)}</span>" for t in s['attack']) or "<span class='tag att'></span>"
    nist = " ".join(f"<span class='tag nist'>{esc(t)}</span>" for t in s['nist'])
    slides.append(f"""
<section class="slide skill">
  <span class="kicker">Skill {s['n']} / 10 · {esc(s['domain'])}</span>
  <h3 dir="rtl">{esc(s['name_ar'])}</h3>
  <h4 class="en">{esc(s['name_en'])}</h4>
  <p class="what" dir="rtl">{esc(s['what_ar'])}</p>
  <p class="what en">{esc(s['what_en'])}</p>
  <div class="cols">
    <div class="col-steps">
      <div class="lbl">Workflow · سير العمل</div>
      <ol>{steps}</ol>
    </div>
    <div class="col-side">
      <div class="lbl">MITRE ATT&amp;CK</div><div class="tags">{attack}</div>
      <div class="lbl">NIST CSF 2.0</div><div class="tags">{nist}</div>
      <div class="lbl">In the lab · في المختبر</div>
      <p class="lab" dir="rtl">{esc(s['lab_ar'])}</p>
      <p class="lab en">{esc(s['lab_en'])}</p>
    </div>
  </div>
</section>""")

# --- Real agent execution results ---
for i, r in enumerate(C.AGENT_RUNS, 1):
    cmd = esc(r["cmd"]).replace("\n","<br>")
    slides.append(f"""
<section class="slide">
  <span class="kicker">Agent Run {i} / {len(C.AGENT_RUNS)} · Executed 2026-08-02</span>
  <h3 class="mono runname">{esc(r['skill'])}</h3>
  <div class="lbl">Command</div>
  <pre class="cmd">{cmd}</pre>
  <div class="lbl">Result · النتيجة</div>
  <p class="res" dir="rtl">{esc(r['result_ar'])}</p>
  <p class="res en">{esc(r['result_en'])}</p>
  <div class="evid">📎 {esc(r['evidence'])}</div>
</section>""")

# --- Verified lab facts ---
factrows = "".join(
    f"<tr><td class='lay'>{esc(k)}</td><td class='mono'>{esc(v)}</td></tr>"
    for k, v in C.LAB_FACTS)
slides.append(f"""
<section class="slide">
  <span class="kicker">Verified · تم التحقق</span>
  <h3 dir="rtl">حقائق المختبر المُتحقَّق منها <span class="en">/ Verified Lab Facts</span></h3>
  <p dir="rtl">كل سطر تم التحقق منه بأمر فعلي على العقدة، ومخرجاته محفوظة في مجلد الأدلة.</p>
  <p class="en">Every row was verified by an actual command on the node, with output saved in the evidence folder.</p>
  <table class="arch t2"><thead><tr><th>Item</th><th>Verified value</th></tr></thead><tbody>{factrows}</tbody></table>
</section>""")

# --- Integrity / honesty slide ---
slides.append("""
<section class="slide">
  <span class="kicker">Methodology · النزاهة العلمية</span>
  <h3 dir="rtl">ما لم ينجح, وكيف عالجناه <span class="en">/ What Did Not Work, and How We Handled It</span></h3>
  <ul class="ethics" dir="rtl">
    <li>فشل إعداد الـ VLAN أولاً بسبب صياغة sed مشوّهة، ثم صُحّح وأُعيد التطبيق حتى صار vlan_filtering=1.
        <span class="en">VLAN setup first failed on a malformed sed directive, then corrected and reapplied until vlan_filtering=1.</span></li>
    <li>فشل الجدار الناري أولاً لاستخدام بادئة IPSet بدل الأسماء المستعارة، ثم صُحّح، ومع آلية تراجع تلقائي تحسّباً لقفل الوصول.
        <span class="en">The firewall first failed using an IPSet prefix instead of aliases, then corrected, with an automatic rollback armed against lockout.</span></li>
    <li>قاعدتان في Suricata لم تُطلقا: قاعدة C2 (لا خادم HTTP في المسار) وقاعدة نفق DNS (عدم مطابقة نمط pcre).
        <span class="en">Two Suricata rules did not fire: the C2 rule (no HTTP server on path) and the DNS-tunneling rule (pcre did not match).</span></li>
    <li>بديلان مبرَّران: جدار Proxmox المدمج بدل pfSense، ومحرّك ارتباط مكافئ بدل Splunk المرخّص.
        <span class="en">Two justified substitutions: Proxmox's built-in firewall instead of pfSense, and an equivalent correlation engine instead of licensed Splunk.</span></li>
    <li>خطوة واحدة غير مكتملة: تفعيل Tailscale يتطلب تسجيل دخول شخصي. والبنية جاهزة والتفعيل بأمر واحد.
        <span class="en">One incomplete step: Tailscale activation requires a personal login. The infrastructure is ready, activation is one command.</span></li>
  </ul>
</section>""")

# --- Lab build ---
lsteps = "".join(f"<li><span class='ar' dir='rtl'>{esc(a)}</span><span class='en'>{esc(e)}</span></li>"
                 for a,e in zip(C.LAB_BUILD['steps_ar'], C.LAB_BUILD['steps_en']))
slides.append(f"""
<section class="slide">
  <span class="kicker">03 · Lab Build</span>
  <h3 dir="rtl">بناء مختبر Proxmox <span class="en">/ Building the Proxmox Lab</span></h3>
  <p dir="rtl"><b>{esc(C.LAB_BUILD['host_ar'])}</b></p>
  <p class="en">{esc(C.LAB_BUILD['host_en'])}</p>
  <ol class="labsteps">{lsteps}</ol>
  <p class="note" dir="rtl"><b>الافتراضية المتداخلة:</b> تشغيل Proxmox (وهو hypervisor) داخل VMware يتطلب <span class="mono">vhv.enable = TRUE</span> وتعطيل Hyper-V على المضيف.</p>
</section>""")

# --- Roadmap ---
phases = "".join(
    f"<div class='phase'><div class='pnum'>{i}</div><div class='pbody'>"
    f"<b dir='rtl'>{esc(ar_t)}</b><span class='en'>{esc(en_t)}</span>"
    f"<p dir='rtl'>{esc(ar_d)}</p><p class='en'>{esc(en_d)}</p></div></div>"
    for i,(ar_t,en_t,ar_d,en_d) in enumerate(C.ROADMAP))
slides.append(f"""
<section class="slide">
  <span class="kicker">03 · Roadmap</span>
  <h3 dir="rtl">خطة النشر المرحلية <span class="en">/ Phased Deployment Roadmap</span></h3>
  <div class="roadmap">{phases}</div>
</section>""")

# --- Ethics / closing ---
slides.append(f"""
<section class="slide">
  <span class="kicker">04 · Ethics &amp; Conclusion</span>
  <h3 dir="rtl">اعتبارات أخلاقية والخلاصة <span class="en">/ Ethics &amp; Conclusion</span></h3>
  <ul class="ethics" dir="rtl">
    <li>جميع الأنشطة دفاعية وتعليمية داخل مختبر معزول تملكه. <span class="en">Defensive &amp; educational, in an isolated lab you own.</span></li>
    <li>لا فحص أو هجوم محاكى ضد أنظمة لا تملك إذن اختبارها. <span class="en">No testing against systems you are not authorized for.</span></li>
    <li>واجهة Proxmox (8006) لا تُفتح للإنترنت, Tailscale فقط. <span class="en">Port 8006 never internet-exposed, Tailscale only.</span></li>
    <li>أنظمة الهدف الضعيفة معزولة خلف pfSense. <span class="en">Vulnerable targets isolated behind pfSense.</span></li>
  </ul>
  <p class="close" dir="rtl">من عزل الشبكة إلى المراقبة والكشف إلى التصليب والخداع: عشر مهارات مربوطة بـ MITRE ATT&amp;CK و NIST CSF في مختبر Proxmox واحد.</p>
  <p class="close en">From isolation to detection to hardening to deception: ten skills mapped to MITRE ATT&amp;CK &amp; NIST CSF in one Proxmox lab.</p>
</section>""")

deck = "\n".join(slides)
n = len(slides)

CSS = """
:root{--navy:#0B2A4A;--teal:#0E7C86;--ink:#12202f;--grey:#5b6472;--bg:#eef2f7;--card:#ffffff;--line:#dbe3ec;--att:#7a1f2b;--attbg:#fbe9eb;--nist:#0d5c47;--nistbg:#e6f3ef;}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"Segoe UI",Tahoma,Arial,sans-serif;background:var(--bg);color:var(--ink);-webkit-font-smoothing:antialiased}
.en{font-style:italic;color:var(--grey)}
.deck{max-width:1180px;margin:0 auto;padding:26px 16px 80px}
.slide{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:44px 52px;margin:0 auto 26px;min-height:600px;box-shadow:0 10px 30px rgba(11,42,74,.07);position:relative;scroll-margin-top:20px}
.slide h1{font-size:2.7rem;color:var(--navy);line-height:1.2;margin:6px 0}
.slide h2{font-size:1.5rem;color:var(--teal);font-weight:600;margin-bottom:18px}
.slide h3{font-size:1.9rem;color:var(--navy);margin-bottom:6px;line-height:1.3}
.slide h3 .en{font-size:1.1rem}
.slide h4{font-size:1.15rem;color:var(--teal);margin-bottom:14px;font-weight:600}
.kicker{display:inline-block;font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;color:#fff;background:var(--teal);padding:5px 14px;border-radius:999px;margin-bottom:16px;font-weight:700}
.slide p{line-height:1.75;margin-bottom:10px;font-size:1.02rem}
/* title */
.title{display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;background:linear-gradient(150deg,#0B2A4A,#12405f 60%,#0E7C86);color:#fff;min-height:640px}
.title h1{color:#fff}.title h2{color:#bfe6ea}
.title .sub{color:#dbe7f2;font-size:1.2rem;max-width:760px}.title .sub.en{color:#a9c7d6}
.title .badge{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.3);padding:7px 16px;border-radius:999px;font-size:.85rem;margin-bottom:26px;letter-spacing:.04em}
.title .meta{margin-top:38px;font-size:.95rem;color:#cfe0ee}.title .meta a{color:#8fd7de;text-decoration:none}
.note{background:#fffaf0;border-inline-start:4px solid #e2a600;padding:12px 16px;border-radius:10px;font-size:.95rem;margin-top:16px}
/* stats */
.statrow{display:flex;gap:16px;margin:22px 0}
.stat{flex:1;background:linear-gradient(160deg,#0B2A4A,#0E7C86);color:#fff;border-radius:14px;padding:20px;text-align:center}
.stat b{display:block;font-size:2.3rem;line-height:1}.stat span{font-size:.9rem;opacity:.85}
/* arch table */
table.arch{width:100%;border-collapse:collapse;margin-top:16px;font-size:1rem}
table.arch th{background:var(--navy);color:#fff;text-align:left;padding:11px 14px}
table.arch td{padding:11px 14px;border-bottom:1px solid var(--line)}
table.arch td.lay{font-weight:700;color:var(--navy)}
table.arch td.sk{font-weight:700;color:var(--teal);white-space:nowrap}
table.arch tr:nth-child(even) td{background:#f6f9fc}
/* skill slide */
.skill .what{font-size:1rem}
.cols{display:grid;grid-template-columns:1.35fr 1fr;gap:26px;margin-top:16px}
.lbl{font-size:.75rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--teal);margin:14px 0 7px}
.col-steps ol{margin:0;padding-inline-start:20px}
.col-steps li{margin-bottom:9px;line-height:1.45}
.col-steps li .ar{display:block;font-size:.96rem}
.col-steps li .en{display:block;font-size:.82rem}
.col-side{background:#f6f9fc;border:1px solid var(--line);border-radius:14px;padding:14px 18px}
.col-side .lbl:first-child{margin-top:0}
.tags{display:flex;flex-wrap:wrap;gap:6px}
.tag{font-size:.78rem;font-weight:700;padding:3px 9px;border-radius:7px;font-family:"Consolas",monospace}
.tag.att{background:var(--attbg);color:var(--att)}
.tag.nist{background:var(--nistbg);color:var(--nist)}
.lab{font-size:.9rem;line-height:1.55;margin-bottom:6px}
/* agent run slides */
.mono{font-family:"Consolas","Courier New",monospace}
.runname{font-size:1.3rem!important;color:var(--teal)!important;word-break:break-all}
pre.cmd{background:#0d1a26;color:#8fe3c0;padding:14px 18px;border-radius:10px;font-family:"Consolas",monospace;font-size:.88rem;line-height:1.6;overflow-x:auto;white-space:pre-wrap;word-break:break-word}
.res{font-size:1rem;line-height:1.7}
.evid{margin-top:14px;display:inline-block;background:var(--nistbg);color:var(--nist);font-family:"Consolas",monospace;font-size:.82rem;padding:7px 13px;border-radius:8px}
table.t2 td.req{font-size:.78rem;color:var(--teal)}
table.t2 td{font-size:.85rem}
.labsteps{margin:14px 0 0;padding-inline-start:22px}
.labsteps li{margin-bottom:10px;line-height:1.5}
.labsteps li .ar{display:block;font-size:.95rem}
.labsteps li .en{display:block;font-size:.8rem}
/* roadmap */
.roadmap{display:flex;flex-direction:column;gap:14px;margin-top:18px}
.phase{display:flex;gap:16px;align-items:flex-start;background:#f6f9fc;border:1px solid var(--line);border-radius:12px;padding:14px 18px}
.pnum{flex:none;width:40px;height:40px;border-radius:50%;background:var(--navy);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:1.1rem}
.pbody b{color:var(--navy);font-size:1.05rem}.pbody .en{margin-inline-start:8px;font-size:.9rem}
.pbody p{font-size:.9rem;margin:2px 0 0}
/* ethics */
.ethics{list-style:none;margin:6px 0 18px}
.ethics li{padding:11px 16px;background:#f6f9fc;border-inline-start:4px solid var(--teal);border-radius:10px;margin-bottom:9px;line-height:1.5}
.ethics li .en{display:block;font-size:.85rem;margin-top:3px}
.close{font-size:1.1rem;font-weight:600;color:var(--navy);margin-top:8px}
.close.en{font-weight:400}
/* nav */
.topbar{position:sticky;top:0;z-index:20;background:rgba(238,242,247,.92);backdrop-filter:blur(6px);border-bottom:1px solid var(--line);padding:9px 16px;display:flex;gap:12px;align-items:center;justify-content:center;flex-wrap:wrap}
.topbar b{color:var(--navy)}
.dots{display:flex;gap:6px;flex-wrap:wrap;justify-content:center}
.dots a{width:11px;height:11px;border-radius:50%;background:#c3cedb;transition:.15s}
.dots a:hover{background:var(--teal);transform:scale(1.25)}
@media print{.topbar{display:none}.slide{box-shadow:none;page-break-after:always;min-height:auto;border:none}body{background:#fff}}
@media(max-width:820px){.cols{grid-template-columns:1fr}.statrow{flex-wrap:wrap}.stat{min-width:44%}.slide{padding:30px 24px}.slide h1{font-size:2rem}}
@media (prefers-color-scheme:dark){:root{--bg:#0c141d;--card:#141f2b;--ink:#e8eef5;--line:#26374a;--grey:#9fb0c2}body{color:var(--ink)}.col-side,.phase,.ethics li,table.arch tr:nth-child(even) td{background:#0f1a25}.note{background:#241f10}}
"""

JS = """
const dots=document.querySelector('.dots');
document.querySelectorAll('.slide').forEach((s,i)=>{s.id='s'+i;const a=document.createElement('a');a.href='#s'+i;a.title='Slide '+(i+1);dots.appendChild(a);});
document.addEventListener('keydown',e=>{const ss=[...document.querySelectorAll('.slide')];let cur=0;const y=window.scrollY;ss.forEach((s,i)=>{if(s.offsetTop-80<=y)cur=i;});if(e.key==='ArrowRight'||e.key==='PageDown'){e.preventDefault();ss[Math.min(cur+1,ss.length-1)].scrollIntoView({behavior:'smooth'});}if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();ss[Math.max(cur-1,0)].scrollIntoView({behavior:'smooth'});}});
"""

DOC = f"""<!doctype html>
<html lang="ar">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Proxmox Security Lab | Presentation</title>
<style>{CSS}</style>
</head>
<body>
<div class="topbar"><b>Proxmox Security Lab</b> · {n} slides · <span class="en">← → to navigate · Ctrl+P to export PDF</span><div class="dots"></div></div>
<div class="deck">
{deck}
</div>
<script>{JS}</script>
</body>
</html>"""

out = r"C:\Users\HP\automation\proxmox-security-lab\Proxmox-Security-Lab-Presentation.html"
open(out,"w",encoding="utf-8").write(DOC)
print("saved", out, len(DOC), "bytes,", n, "slides")
