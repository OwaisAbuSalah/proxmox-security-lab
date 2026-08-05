# Agent Lab — تنفيذ المهارات عبر وكيل ذكاء اصطناعي
**AI-Agent Execution Lab** · Anthropic Cybersecurity Skills

مصدر المهارات: https://github.com/mukul975/Anthropic-Cybersecurity-Skills (Apache-2.0)

---

## الفكرة / Concept

كل مهارة في الريبو ليست وثيقة فقط — بل **وكيل قابل للتشغيل**:

```
skills/<skill-name>/
├── SKILL.md              # ترويسة YAML (اكتشاف) + خطوات Markdown (تنفيذ)
├── scripts/agent.py      # الوكيل القابل للتشغيل
└── references/           # مراجع تقنية
```

ومجلد `.claude-plugin/` يسجّل المجموعة كإضافة (plugin) لـ Claude Code، فيكتشف الوكيل
المهارة المناسبة من ترويسة YAML ثم ينفّذ `agent.py`.

---

## المستوى الأول — وكلاء نُفِّذوا فعلياً على المضيف
**Tier 1 — agents executed on the host (2026-08-02)**

### 1. DNS Exfiltration Detection
```bash
python skills/analyzing-dns-logs-for-exfiltration/scripts/agent.py
```
**النتيجة:** كشف نفق DNS على `evil-tunnel.com` (50 استعلام، متوسط طول subdomain = 60)،
نطاق DGA بإنتروبي `3.9069`، وإساءة TXT من `192.168.1.105`.
📎 `evidence/01_dns_exfiltration_agent.txt`

### 2. Ransomware Canary Files
```bash
# نشر
python skills/deploying-ransomware-canary-files/scripts/agent.py \
    --action deploy --dirs sandbox/finance sandbox/hr
# مراقبة لحظية (watchdog)
python skills/deploying-ransomware-canary-files/scripts/agent.py --action monitor
# فحص السلامة
python skills/deploying-ransomware-canary-files/scripts/agent.py --action verify
```
**النتيجة:** 16 ملف canary مع بصمات SHA-256. عند محاكاة التشفير وإعادة التسمية إلى `.LOCKED`
أطلق الوكيل تنبيهين `CRITICAL` خلال أجزاء من الثانية، وأكّد الفحص: **14 سليم / 2 مفقود**.
📎 `evidence/02_canary_agent.txt` · `evidence/03_canary_live_monitor.txt`

### 3. SBOM Supply-Chain Analysis
```bash
python skills/analyzing-sbom-for-supply-chain-vulnerabilities/scripts/agent.py \
    parse   sboms/host-python.cdx.json
python skills/analyzing-sbom-for-supply-chain-vulnerabilities/scripts/agent.py \
    analyze sboms/host-python.cdx.json --output evidence/sbom_report.json
```
**النتيجة:** SBOM حقيقي (CycloneDX 1.5) من **75 حزمة مثبّتة فعلياً**، تحليل مقابل NVD الحيّة:
**9 مكوّنات مصابة، 19 ثغرة** (1 حرجة، 13 عالية، 5 متوسطة).

> ⚠️ **ملاحظة تحليلية مهمة:** بعض النتائج **إيجابيات كاذبة (false positives)** بسبب المطابقة
> بالاسم لا بالـ CPE الدقيق — مثلاً `click@8.4.1` طابق ثغرة إضافة ووردبريس، و`pip` طابق ثغرة
> conda-build. هذا يوضّح لماذا يحتاج ترتيب الثغرات إلى **سياق الأصل** لا الاعتماد على CVSS وحده.

📎 `evidence/04_sbom_agent.txt` · `evidence/sbom_report.json`

### 4. TLS 1.3 Audit
```bash
python skills/configuring-tls-1-3-for-secure-communications/scripts/agent.py \
    --host www.proxmox.com --port 443 --output evidence/tls_proxmox.json
```
**النتيجة (proxmox.com):** TLS 1.0/1.1 معطّلان، TLS 1.2/1.3 مدعومان، شهادة Let's Encrypt
تنتهي خلال 50 يوماً، تفاوض على `TLS_AES_256_GCM_SHA384` عبر TLS 1.3.
📎 `evidence/05_tls_agent.txt` · `evidence/tls_proxmox.json` · `evidence/tls_github.json`

### 5. Suricata Status (حدّ المستوى الأول)
```bash
python skills/configuring-suricata-for-network-monitoring/scripts/agent.py status
```
**النتيجة:** `{"installed": false, "running": false}` — نتيجة **صحيحة ومتوقعة** على ويندوز،
لأن Suricata نظام كشف يعمل على Linux. توضّح بدقة الحد الفاصل نحو المستوى الثاني.
📎 `evidence/06_suricata_agent_pre_lab.txt`

---

## المستوى الثاني — وكلاء يتطلبون مختبر Proxmox
**Tier 2 — agents requiring lab infrastructure**

| Skill | يتطلّب / Requires |
|---|---|
| `configuring-network-segmentation-with-vlans` | `netmiko` → مبدّل مُدار / VLAN bridges |
| `configuring-pfsense-firewall-rules` | pfSense REST API (`--url --api-key --api-secret`) |
| `configuring-suricata-for-network-monitoring` | Suricata 7.x على Linux |
| `analyzing-security-logs-with-splunk` | `splunklib` → منفذ إدارة Splunk 8089 |
| `building-vulnerability-scanning-workflow` | `python-nmap` + OpenVAS/Nessus + أنظمة هدف |

**هذا هو سبب بناء مختبر Proxmox** — لتوفير البنية التحتية التي يحتاجها هؤلاء الوكلاء.

---

## المتطلبات / Dependencies

```bash
pip install watchdog requests psutil cryptography
```

للمستوى الثاني (داخل المختبر): `netmiko`, `python-nmap`, `splunk-sdk`

---

## إعادة التنفيذ / Reproduce

```bash
cd agent-lab
python skills/analyzing-dns-logs-for-exfiltration/scripts/agent.py
python skills/deploying-ransomware-canary-files/scripts/agent.py --action deploy --dirs sandbox/finance sandbox/hr
python skills/analyzing-sbom-for-supply-chain-vulnerabilities/scripts/agent.py analyze sboms/host-python.cdx.json
python skills/configuring-tls-1-3-for-secure-communications/scripts/agent.py --host www.proxmox.com
```

---

## ⚠️ نطاق أخلاقي / Ethical Scope

جميع الأنشطة **دفاعية (blue-team)** داخل بيئة معزولة مملوكة. ملفات الـ canary وهمية بالكامل
(بيانات اعتماد مزيفة مولّدة عشوائياً)، ومحاكاة التشفير تمّت داخل `sandbox/` فقط.
فحوصات TLS استهدفت خوادم عامة بقراءة الشهادة فقط (لا اختبار اختراق).
