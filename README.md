# Proxmox Security Lab — 10 Defensive Skills Executed by an AI Agent

مشروع مختبر أمني على Proxmox VE: تطبيق عشر مهارات دفاعية من مكتبة
[Anthropic Cybersecurity Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)
عبر وكيل ذكاء اصطناعي، مع تقرير وعرض تقديمي.

A home security lab built on Proxmox VE. Ten defensive skills from the Anthropic
Cybersecurity Skills library were executed through an AI agent, with a bilingual
report and slide deck produced from the results.

---

## What was actually built

Proxmox VE 9.2.2 was installed as a virtual machine on VMware Workstation 25 with
nested virtualisation enabled, giving a real hypervisor with `/dev/kvm` available
inside it. Every skill below was run against that node or on the host, and the raw
output of each run is kept in [`agent-lab/evidence/`](agent-lab/evidence).

| # | Skill | Domain | Result |
|---|-------|--------|--------|
| 1 | Network segmentation with VLANs | Network Security | 3 isolated zones + 802.1Q trunk (`vlan_filtering=1`) |
| 2 | Firewall rules (pfSense workflow) | Network Security | Deny-by-default policy, verified in iptables |
| 3 | Suricata IDS/IPS | Network Security | 7.0.10 + 5 custom rules, 6 real alerts |
| 4 | Tailscale zero-trust VPN | Zero Trust | 1.98.10 installed, WireGuard loaded |
| 5 | TLS 1.3 configuration | Cryptography | Live audit of the Proxmox UI |
| 6 | Security log analysis (SIEM) | Incident Response | 26 events correlated across 2 sources |
| 7 | DNS exfiltration analysis | SOC Operations | 2 tunnels found in 36 real Suricata events |
| 8 | Vulnerability scanning workflow | Vulnerability Mgmt | 4 hosts, service enumeration, 61 pending updates |
| 9 | Ransomware canary files | Deception | 16 canaries, encryption detected in milliseconds |
| 10 | SBOM supply-chain analysis | Supply Chain | 75 packages checked against live NVD |

### Detection chain

The strongest single result is an end-to-end chain rather than any one skill:

```
simulated attack  ->  Suricata capture  ->  DNS analysis agent  ->  confirmed detection
```

36 DNS events captured by Suricata on the node were fed to the DNS exfiltration
agent, which identified both tunnels by subdomain length and query volume.

---

## Layout

```
├── content.py            # single source of truth for all report/deck text
├── build_docx.py         # generates the Word report
├── build_html.py         # generates the HTML slide deck
├── agent-lab/
│   ├── skills/           # the 10 skills (Apache-2.0, from the upstream library)
│   └── evidence/         # raw output of every agent run
├── Proxmox-Security-Lab-Report.docx
└── Proxmox-Security-Lab-Presentation.html
```

Regenerate both deliverables after editing `content.py`:

```bash
python build_docx.py && python build_html.py
```

---

## Substitutions and limitations

Three things did not go exactly to plan, and the report documents them rather than
hiding them:

- **pfSense** needs its own VM with two NICs, which the lab could not spare, so the
  same zone policy was implemented with Proxmox's built-in firewall.
- **Splunk Enterprise** requires a licensed server, so the correlation logic the
  skill describes was applied directly to the lab's own logs.
- **Tailscale** is installed and running, but `tailscale up` needs an identity
  provider login tied to a personal account, so activation was left undone.

Two of the five Suricata rules also stayed silent during testing, for reasons
explained in the report.

---

## Scope

Everything here is defensive and was carried out inside an isolated lab. No scan or
simulated attack was directed at any system outside it. The `agent-lab/skills/`
directory is redistributed from the upstream project under Apache 2.0.
