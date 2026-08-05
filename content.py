# -*- coding: utf-8 -*-
"""Shared bilingual content for the Proxmox Security Lab report + presentation.
Source: https://github.com/mukul975/Anthropic-Cybersecurity-Skills
"""

PROJECT = {
    "title_ar": "تطبيق وقياس ضوابط دفاعية على مختبر افتراضي وفق MITRE ATT&CK و NIST CSF 2.0",
    "title_en": "Implementing and Measuring Defensive Controls in a Virtual Lab, Mapped to MITRE ATT&CK and NIST CSF 2.0",
    "subtitle_ar": "تنفيذ عشر مهارات دفاعية عبر وكيل ذكاء اصطناعي على عقدة Proxmox VE",
    "subtitle_en": "Ten defensive skills executed through an AI agent on a Proxmox VE node",
    "author": "owaisabusalah@gmail.com",
    "date": "2026-08-02",
    "repo": "https://github.com/mukul975/Anthropic-Cybersecurity-Skills",
}

# Intro paragraphs (each: ar, en)
INTRO = {
    "about_repo_ar": (
        "مكتبة Anthropic Cybersecurity Skills قاعدة معرفة مفتوحة المصدر تحت رخصة Apache 2.0، وفيها 817 مهارة "
        "أمن سيبراني موزّعة على 29 مجالاً. كل مهارة مكتوبة بصيغة موحّدة تتبع معيار agentskills.io: ترويسة YAML "
        "مختصرة في أعلى الملف تتيح البحث السريع، يليها شرح بصيغة Markdown يوضّح خطوات التنفيذ. الميزة الأهم أن كل "
        "مهارة مربوطة بأطر معيارية معروفة مثل MITRE ATT&CK و NIST CSF 2.0 و D3FEND، وهو ما يسمح بقياس التغطية "
        "الدفاعية بدل الاكتفاء بوصفها."
    ),
    "about_repo_en": (
        "The Anthropic Cybersecurity Skills library is an open-source knowledge base released under Apache 2.0. It holds "
        "817 security skills spread across 29 domains. Every skill uses the same layout, following the agentskills.io "
        "standard: a short YAML header for fast lookup, then a Markdown body describing how to carry the work out. What "
        "makes it useful is that each skill carries mappings to recognised frameworks such as MITRE ATT&CK, NIST CSF 2.0 "
        "and D3FEND, so defensive coverage can be measured rather than just described."
    ),
    "why_proxmox_ar": (
        "وقع الاختيار على Proxmox VE لأنه منصة افتراضية كاملة تعمل بشكل متواصل وتشغّل عدة أنظمة وحاويات معزولة على "
        "جهاز واحد. هذه الخاصية تحديداً هي ما يجعله مناسباً لمحاكاة شبكة مؤسسة مصغّرة تضم جداراً نارياً وخوادم وأدوات "
        "مراقبة وأنظمة هدف، مع بقاء الكل معزولاً عن شبكة المنزل. ويجدر التنبيه إلى أن Proxmox يُثبَّت كنظام تشغيل "
        "مستقل على الجهاز، لا كبرنامج يعمل فوق ويندوز."
    ),
    "why_proxmox_en": (
        "Proxmox VE was chosen because it is a full virtualisation platform that runs continuously and hosts several "
        "isolated systems and containers on one machine. That property is exactly what makes it suitable for simulating a "
        "small enterprise network with a firewall, servers, monitoring tools and target systems, while keeping all of it "
        "away from the home network. It is worth noting that Proxmox installs as its own operating system on the machine, "
        "not as an application running on top of Windows."
    ),
    "scope_ar": (
        "نطاق العمل في هذا التقرير دفاعي بالكامل. كل ما نُفِّذ جرى داخل مختبر معزول نملكه ونملك صلاحية اختباره، "
        "ولم يُوجَّه أي فحص أو محاكاة هجوم نحو نظام أو شبكة خارج هذا النطاق."
    ),
    "scope_en": (
        "The work in this report is entirely defensive in nature. Everything was carried out inside an isolated lab we own "
        "and are authorised to test, and no scan or simulated attack was aimed at any system or network outside it."
    ),
    "agent_method_ar": (
        "المهارات في هذا المشروع لم تُقرأ فحسب، بل نُفِّذت عبر وكيل ذكاء اصطناعي. والريبو مبني لهذا الغرض أصلاً: "
        "مجلد .claude-plugin يسجّله كإضافة تعمل داخل Claude Code، وكل مهارة تحتوي ملف scripts/agent.py وهو برنامج "
        "قابل للتشغيل ينفّذ خطواتها. يقرأ الوكيل ترويسة YAML ليحدّد المهارة المناسبة للمهمة، ثم يشغّل ملف الوكيل "
        "بالمعاملات الملائمة ويقرأ المخرجات ويبني عليها قراره التالي."
    ),
    "agent_method_en": (
        "The skills in this project were not merely read; they were executed through an AI agent. The repository is built "
        "for that: a .claude-plugin directory registers it as an extension inside Claude Code, and each skill ships a "
        "scripts/agent.py, a runnable program that performs its steps. The agent reads the YAML header to pick the skill "
        "that fits the task, runs the agent file with suitable arguments, then reads the output and decides what to do next."
    ),
    "tiers_ar": (
        "نُفِّذت المهارات العشر كلها، وجرى ذلك على مرحلتين. في المرحلة الأولى شُغِّلت خمس مهارات على جهاز المضيف قبل "
        "أن تكون البنية التحتية جاهزة. أما المرحلة الثانية فنُفِّذت داخل عقدة Proxmox VE 9.2.2 حقيقية أقمناها على "
        "VMware Workstation بعد تفعيل المحاكاة المتداخلة والتأكد من توفّر /dev/kvm. وكل مخرَج في مجلد evidence/ ناتج "
        "عن تشغيل فعلي، لا عن مثال توضيحي."
    ),
    "tiers_en": (
        "All ten skills were executed, and this happened in two stages. In the first, five skills ran on the host machine "
        "before any infrastructure existed. The second stage took place inside a real Proxmox VE 9.2.2 node built on VMware "
        "Workstation, once nested virtualisation was enabled and /dev/kvm confirmed. Every output in evidence/ comes from an "
        "actual run rather than an illustrative sample."
    ),
    "lab_build_ar": (
        "أُقيم المختبر على النحو التالي: ثُبِّت Proxmox VE 9.2.2 كجهاز افتراضي على VMware Workstation 25، بعد التحقق من "
        "بصمة SHA-256 لملف الـ ISO ومطابقتها للنسخة المنشورة رسمياً. خُصِّص للعقدة 6 غيغابايت من الذاكرة وأربعة أنوية "
        "معالجة وقرص سعته 80 غيغابايت، على شبكة NAT. تعمل العقدة على العنوان 192.168.29.132 وواجهة إدارتها على المنفذ "
        "8006، وأُتيح للوكيل وصول آلي عبر مفتاح SSH من نوع ed25519 دون استخدام كلمات مرور."
    ),
    "lab_build_en": (
        "The lab was set up as follows. Proxmox VE 9.2.2 was installed as a virtual machine on VMware Workstation 25, after "
        "checking the ISO's SHA-256 fingerprint against the officially published release. The node was given 6 GB of memory, "
        "four processor cores and an 80 GB disk on a NAT network. It runs at 192.168.29.132 with its management interface on "
        "port 8006, and the agent was given automated access through an ed25519 SSH key, with no passwords used."
    ),
}

# Real, verified agent executions (Tier 1) - evidence captured 2026-08-02
AGENT_RUNS = [
    {
        "skill": "analyzing-dns-logs-for-exfiltration",
        "cmd": "python skills/analyzing-dns-logs-for-exfiltration/scripts/agent.py",
        "evidence": "evidence/01_dns_exfiltration_agent.txt",
        "result_ar": "كشف الوكيل نفق DNS على النطاق evil-tunnel.com (50 استعلام، متوسط طول النطاق الفرعي 60 حرفاً)، "
                     "ونطاق DGA بإنتروبي 3.9069، وإساءة استخدام سجلات TXT من المصدر 192.168.1.105.",
        "result_en": "The agent detected DNS tunneling on evil-tunnel.com (50 queries, avg subdomain length 60), a DGA "
                     "domain at entropy 3.9069, and TXT-record abuse from source 192.168.1.105.",
    },
    {
        "skill": "deploying-ransomware-canary-files",
        "cmd": "agent.py --action deploy --dirs sandbox/finance sandbox/hr\nagent.py --action monitor\nagent.py --action verify",
        "evidence": "evidence/02_canary_agent.txt, evidence/03_canary_live_monitor.txt",
        "result_ar": "نشر الوكيل 16 ملف canary مع بصمات SHA-256، ثم شغّلنا مراقب watchdog اللحظي. عند محاكاة تشفير "
                     "ملفين وإعادة تسميتهما بامتداد .LOCKED، أطلق الوكيل تنبيهين CRITICAL خلال أجزاء من الثانية، "
                     "وأكّد فحص السلامة النتيجة: 14 سليم و2 مفقود.",
        "result_en": "The agent deployed 16 canary files with SHA-256 baselines; we then ran the live watchdog monitor. "
                     "When two files were encrypted and renamed to .LOCKED, the agent raised two CRITICAL alerts within "
                     "milliseconds, and integrity verification confirmed it: 14 intact, 2 missing.",
    },
    {
        "skill": "analyzing-sbom-for-supply-chain-vulnerabilities",
        "cmd": "agent.py parse sboms/host-python.cdx.json\nagent.py analyze sboms/host-python.cdx.json --output report.json",
        "evidence": "evidence/04_sbom_agent.txt, evidence/sbom_report.json",
        "result_ar": "ولّدنا SBOM حقيقياً بصيغة CycloneDX 1.5 من 75 حزمة مثبّتة فعلياً، وحلّله الوكيل مقابل قاعدة NVD "
                     "الحيّة: 9 مكوّنات مصابة و19 ثغرة (1 حرجة، 13 عالية، 5 متوسطة). ملاحظة مهمة: بعض النتائج إيجابيات "
                     "كاذبة بسبب المطابقة بالاسم (CPE). ومن أمثلة ذلك ربط click@8.4.1 بثغرة إضافة ووردبريس.",
        "result_en": "We generated a real CycloneDX 1.5 SBOM from 75 actually-installed packages; the agent analyzed it "
                     "against the live NVD database: 9 vulnerable components, 19 CVEs (1 critical, 13 high, 5 medium). "
                     "Key finding: some results are false positives from CPE name-matching. One example is click@8.4.1 matched a "
                     "WordPress plugin CVE.",
    },
    {
        "skill": "configuring-tls-1-3-for-secure-communications",
        "cmd": "agent.py --host www.proxmox.com --port 443 --output tls_proxmox.json",
        "evidence": "evidence/05_tls_agent.txt, evidence/tls_proxmox.json",
        "result_ar": "دقّق الوكيل إعداد TLS لموقعين حقيقيين. النتيجة لـ proxmox.com: TLS 1.0 و1.1 معطّلان، "
                     "TLS 1.2/1.3 مدعومان، الشهادة من Let's Encrypt وتنتهي خلال 50 يوماً، والتفاوض تم على "
                     "TLS_AES_256_GCM_SHA384 عبر TLS 1.3. وهو الإعداد المرجعي الذي سنطبّقه على واجهة Proxmox.",
        "result_en": "The agent audited TLS on two real endpoints. For proxmox.com: TLS 1.0/1.1 disabled, TLS 1.2/1.3 "
                     "supported, Let's Encrypt certificate expiring in 50 days, negotiated TLS_AES_256_GCM_SHA384 over "
                     "TLS 1.3. the reference configuration we will apply to the Proxmox UI.",
    },
    {
        "skill": "configuring-suricata-for-network-monitoring",
        "cmd": "agent.py status",
        "evidence": "evidence/06_suricata_agent_pre_lab.txt",
        "result_ar": (
            "قبل بناء المختبر شغّلنا وكيل Suricata على جهاز ويندوز للتحقق من حالته، فأعاد نتيجة سالبة متوقّعة: الأداة غير "
            "مثبّتة ولا تعمل. Suricata نظام كشف اختراق يعمل على Linux ويحتاج واجهة شبكة حقيقية لالتقاط المرور، وهو ما لا "
            "يوفّره المضيف. هذه النتيجة تحديداً هي التي دفعتنا إلى بناء عقدة Proxmox، حيث نُفِّذت المهارة لاحقاً بالكامل."
        ),
        "result_en": (
            "Before the lab existed we ran the Suricata agent on the Windows host to check its status, and it returned "
            "the expected negative result: not installed, not running. Suricata is a Linux intrusion detection system and "
            "needs a real network interface to capture traffic, which the host could not provide. That result is "
            "precisely what prompted building the Proxmox node, where the skill was later carried out in full."
        ),
    },
]

# Tier 2 - agents that require the Proxmox lab infrastructure
TIER2 = [
    ("configuring-network-segmentation-with-vlans", "netmiko → managed switch / Proxmox VLAN bridges",
     "يتصل بمبدّلات مُدارة عبر SSH لتطبيق الـ VLANs", "Connects to managed switches over SSH to apply VLANs"),
    ("configuring-pfsense-firewall-rules", "pfSense REST API (--url --api-key --api-secret)",
     "يحتاج pfSense مثبّتاً كـ VM مع تفعيل الـ API", "Requires pfSense installed as a VM with its API enabled"),
    ("configuring-suricata-for-network-monitoring", "Suricata 7.x on Linux",
     "يحتاج Suricata على Ubuntu VM مع واجهة مراقبة", "Requires Suricata on an Ubuntu VM with a monitoring interface"),
    ("analyzing-security-logs-with-splunk", "splunklib → Splunk management port 8089",
     "يحتاج خادم Splunk/Wazuh يعمل داخل المختبر", "Requires a running Splunk/Wazuh server in the lab"),
    ("building-vulnerability-scanning-workflow", "python-nmap + OpenVAS/Nessus",
     "يحتاج nmap وماسح ثغرات وأنظمة هدف", "Requires nmap, a vulnerability scanner, and target systems"),
]

# Lab build - real VMware Workstation environment prepared on this machine
LAB_BUILD = {
    "host_ar": "المضيف: Intel Core i7-12700 (12 نواة / 20 خيط)، 16 GB RAM، Windows 11 Pro، VMware Workstation 25.",
    "host_en": "Host: Intel Core i7-12700 (12 cores / 20 threads), 16 GB RAM, Windows 11 Pro, VMware Workstation 25.",
    "steps_ar": [
        "التحقق من دعم المعالج للـ virtualization (VT-x مفعّل) وتأكيد أن Hyper-V غير مُشغّل (hypervisorlaunchtype = Off) لتعمل الافتراضية المتداخلة (nested virtualization)",
        "تحميل صورة Proxmox VE 9.2-1 الرسمية (1.59 GB) إلى D:\\ProxmoxLab\\ISO",
        "إنشاء قرص افتراضي 80 GB بصيغة LSI Logic SCSI عبر vmware-vdiskmanager",
        "كتابة ملف الإعداد Proxmox-VE.vmx مع vhv.enable = TRUE (الافتراضية المتداخلة)، 6 GB RAM، 4 vCPU، وشبكة NAT",
        "تشغيل المثبّت وتعيين عنوان ثابت 192.168.29.10/24 والبوابة 192.168.29.2",
        "الوصول إلى الواجهة على https://192.168.29.10:8006 بحساب root وواقع Linux PAM",
    ],
    "steps_en": [
        "Verify CPU virtualization support (VT-x enabled) and confirm Hyper-V is off (hypervisorlaunchtype = Off) so nested virtualization works",
        "Download the official Proxmox VE 9.2-1 image (1.59 GB) to D:\\ProxmoxLab\\ISO",
        "Create an 80 GB LSI Logic SCSI virtual disk with vmware-vdiskmanager",
        "Write Proxmox-VE.vmx with vhv.enable = TRUE (nested virtualization), 6 GB RAM, 4 vCPU, NAT networking",
        "Run the installer and assign static address 192.168.29.10/24, gateway 192.168.29.2",
        "Reach the web UI at https://192.168.29.10:8006 as root with the Linux PAM realm",
    ],
}

# The 10 skills. Each dict fully bilingual.
SKILLS = [
    {
        "n": 1,
        "slug": "configuring-network-segmentation-with-vlans",
        "name_en": "Configuring Network Segmentation with VLANs",
        "name_ar": "تقسيم الشبكة باستخدام VLANs",
        "domain": "Network Security",
        "attack": ["T1046", "T1040", "T1557.002", "T1021", "T1018"],
        "nist": ["PR.IR-01", "DE.CM-01", "ID.AM-03", "PR.DS-02"],
        "what_ar": "تصميم وتطبيق تقسيم الشبكة إلى مناطق معزولة (VLANs) عبر معيار 802.1Q لعزل النطاقات وتقليل مساحة الهجوم ومنع الحركة الجانبية (lateral movement).",
        "what_en": "Design and implement VLAN-based segmentation (802.1Q) to isolate zones, shrink the attack surface, and block lateral movement between segments.",
        "steps_ar": [
            "تصميم معمارية VLAN حسب المناطق الأمنية (خوادم، إدارة، IoT، ضيوف، DMZ)",
            "تعريف الـ VLANs وربط كل منفذ (port) بالـ VLAN المناسب",
            "إعداد روابط trunk 802.1Q بين المبدلات",
            "تطبيق ACLs للتحكم في التوجيه بين الـ VLANs",
            "تقوية المبدل ضد هجمات VLAN Hopping (تعطيل DTP، native VLAN مخصصة)",
        ],
        "steps_en": [
            "Design a VLAN architecture by security zone (servers, management, IoT, guest, DMZ)",
            "Define VLANs and map each switch port to the correct VLAN",
            "Configure 802.1Q trunk links between switches",
            "Apply ACLs to control inter-VLAN routing",
            "Harden the switch against VLAN-hopping (disable DTP, dedicated native VLAN)",
        ],
        "lab_ar": "في Proxmox نُنشئ جسوراً (Linux bridges) موسومة بـ VLAN tags (vmbr0.10، vmbr0.20...) لعزل شبكة الإدارة عن شبكة الخوادم وشبكة الأنظمة الهدف.",
        "lab_en": "In Proxmox we create VLAN-tagged Linux bridges (vmbr0.10, vmbr0.20…) to isolate the management network from the server network and the target/vulnerable systems.",
    },
    {
        "n": 2,
        "slug": "configuring-pfsense-firewall-rules",
        "name_en": "Configuring pfSense Firewall Rules",
        "name_ar": "إعداد قواعد جدار pfSense الناري",
        "domain": "Network Security",
        "attack": ["T1071.001", "T1095", "T1572", "T1571", "T1041"],
        "nist": ["PR.IR-01", "DE.CM-01", "ID.AM-03", "PR.DS-02"],
        "what_ar": "إعداد جدار pfSense الناري: قواعد المرور، سياسات NAT، أنفاق VPN، وتشكيل المرور لفرض العزل بين النطاقات.",
        "what_en": "Configure pfSense firewall rules, NAT policies, VPN tunnels, and traffic shaping to enforce segmentation and control traffic flow between zones.",
        "steps_ar": [
            "تعريف الواجهات (WAN/LAN/VLANs) في WebConfigurator",
            "إنشاء aliases للمضيفات والمنافذ لتبسيط القواعد",
            "كتابة قواعد default-deny ثم السماح المحدد، مع تسجيل الحزم المرفوضة",
            "إعداد NAT / port forwarding للخدمات المكشوفة بحذر",
            "إعداد VPN (IPsec/OpenVPN) للوصول الآمن",
        ],
        "steps_en": [
            "Define interfaces (WAN/LAN/VLANs) in the WebConfigurator",
            "Create host/port aliases to simplify rules",
            "Write default-deny rules then explicit allows, logging blocked packets",
            "Configure NAT / port-forwarding for exposed services cautiously",
            "Set up VPN (IPsec/OpenVPN) for secure access",
        ],
        "lab_ar": "نُشغّل pfSense كـ VM داخل Proxmox بواجهتين (WAN + LAN) لتكون بوّابة المختبر، وتفرض العزل بين الـ VLANs التي أنشأناها في المهارة الأولى.",
        "lab_en": "We run pfSense as a Proxmox VM with two interfaces (WAN + LAN) as the lab gateway, enforcing isolation between the VLANs created in Skill 1.",
    },
    {
        "n": 3,
        "slug": "configuring-suricata-for-network-monitoring",
        "name_en": "Configuring Suricata for Network Monitoring (IDS/IPS)",
        "name_ar": "إعداد Suricata لمراقبة الشبكة (IDS/IPS)",
        "domain": "Network Security",
        "attack": ["T1046", "T1071.001", "T1572", "T1048", "T1573.001"],
        "nist": ["PR.IR-01", "DE.CM-01", "ID.AM-03", "PR.DS-02"],
        "what_ar": "نشر وإعداد Suricata كنظام كشف/منع اختراق مع قواعد Emerging Threats وسجلات EVE JSON للتفتيش اللحظي لحركة الشبكة.",
        "what_en": "Deploy Suricata IDS/IPS with Emerging Threats rulesets and EVE JSON logging for real-time, protocol-aware traffic inspection and SIEM integration.",
        "steps_ar": [
            "تثبيت Suricata 7.0+ وأداة suricata-update",
            "ربط واجهة الالتقاط بمنفذ SPAN أو جسر inline",
            "تفعيل AF_PACKET وتحميل قواعد ET Open",
            "تفعيل مخرجات EVE JSON (أحداث، HTTP، TLS، DNS، flow)",
            "كتابة قواعد مخصصة ودمج السجلات في الـ SIEM",
        ],
        "steps_en": [
            "Install Suricata 7.0+ and the suricata-update tool",
            "Attach the capture interface to a SPAN port or inline bridge",
            "Enable AF_PACKET and load the ET Open ruleset",
            "Enable EVE JSON outputs (alerts, HTTP, TLS, DNS, flow)",
            "Write custom rules and forward logs to the SIEM",
        ],
        "lab_ar": "نضع Suricata على واجهة span داخل Proxmox تراقب مرور شبكة الأنظمة الهدف، وتُغذّي سجلات EVE للـ SIEM في المهارة 6.",
        "lab_en": "We place Suricata on a span interface in Proxmox watching the target-network traffic and feed its EVE logs into the SIEM from Skill 6.",
    },
    {
        "n": 4,
        "slug": "deploying-tailscale-for-zero-trust-vpn",
        "name_en": "Deploying Tailscale for Zero-Trust VPN",
        "name_ar": "نشر Tailscale كـ VPN بمبدأ Zero Trust",
        "domain": "Zero Trust Architecture",
        "attack": ["T1133", "T1078", "T1021", "T1572"],
        "nist": ["PR.AA-01", "PR.AA-05", "PR.IR-01", "GV.PO-01"],
        "what_ar": "نشر Tailscale (مبني على WireGuard) كشبكة VPN متشابكة بثقة صفرية، مع تحكم وصول مبني على الهوية (ACLs) وعقد خروج (exit nodes).",
        "what_en": "Deploy Tailscale (WireGuard-based) as a zero-trust mesh VPN with identity-aware ACLs and exit nodes for secure peer-to-peer connectivity.",
        "steps_ar": [
            "ربط Tailscale بمزوّد هوية (Google/GitHub/OIDC)",
            "تثبيت العميل على الأجهزة وتكوين الـ tailnet",
            "كتابة سياسات ACL دقيقة (من يصل إلى ماذا)",
            "تفعيل subnet router للوصول إلى شبكة المختبر دون فتح منافذ",
            "(اختياري) تشغيل Headscale ذاتي الاستضافة",
        ],
        "steps_en": [
            "Connect Tailscale to an identity provider (Google/GitHub/OIDC)",
            "Install the client on devices and form the tailnet",
            "Write granular ACL policies (who reaches what)",
            "Enable a subnet router to reach the lab without opening ports",
            "(Optional) Run self-hosted Headscale",
        ],
        "lab_ar": "يعالج هذا مباشرة تحذير دليل Proxmox: لا تفتح المنفذ 8006 للإنترنت. نصل إلى واجهة Proxmox والـ VMs من خارج المنزل عبر tailnet مشفّر بدلاً من كشف الخدمة.",
        "lab_en": "This directly answers the Proxmox guide's warning: never expose port 8006 to the internet. We reach the Proxmox UI and VMs from outside the home over an encrypted tailnet instead of exposing the service.",
    },
    {
        "n": 5,
        "slug": "configuring-tls-1-3-for-secure-communications",
        "name_en": "Configuring TLS 1.3 for Secure Communications",
        "name_ar": "إعداد TLS 1.3 للاتصالات الآمنة",
        "domain": "Cryptography",
        "attack": ["T1557", "T1040", "T1573.002", "T1539", "T1556.004"],
        "nist": ["PR.DS-01", "PR.DS-02", "PR.DS-10"],
        "what_ar": "إعداد TLS 1.3 (RFC 8446) على الخوادم مع سرية تقدمية تامة (PFS)، وتعطيل الإصدارات والخوارزميات الضعيفة، والتحقق من الإعداد.",
        "what_en": "Configure TLS 1.3 (RFC 8446) on servers with perfect forward secrecy, disable legacy versions/weak ciphers, and validate the configuration.",
        "steps_ar": [
            "تفعيل TLS 1.3 فقط على nginx/Apache وتعطيل 1.0/1.1",
            "اختيار مجموعات تشفير TLS 1.3 الآمنة",
            "إدارة الشهادات (ذاتية التوقيع للمختبر أو Let's Encrypt)",
            "التحقق بـ openssl و testssl.sh",
            "ضبط 0-RTT early data بحمايات مناسبة",
        ],
        "steps_en": [
            "Enable TLS 1.3 only on nginx/Apache, disable 1.0/1.1",
            "Select secure TLS 1.3 cipher suites",
            "Manage certificates (self-signed for lab or Let's Encrypt)",
            "Validate with openssl and testssl.sh",
            "Tune 0-RTT early data with proper protections",
        ],
        "lab_ar": "نستبدل شهادة Proxmox الذاتية الافتراضية بإعداد TLS 1.3 قوي، ونضع reverse proxy بـ nginx أمام واجهة 8006 لإنهاء TLS بشكل سليم.",
        "lab_en": "We replace Proxmox's default self-signed cert with a strong TLS 1.3 setup and put an nginx reverse proxy in front of the 8006 UI for clean TLS termination.",
    },
    {
        "n": 6,
        "slug": "analyzing-security-logs-with-splunk",
        "name_en": "Analyzing Security Logs with Splunk (SIEM)",
        "name_ar": "تحليل السجلات الأمنية بـ Splunk (SIEM)",
        "domain": "Incident Response / SIEM",
        "attack": ["T1110", "T1550.002", "T1021.001", "T1059.001", "T1003.001"],
        "nist": ["RS.MA-01", "RS.MA-02", "RS.AN-03", "RC.RP-01"],
        "what_ar": "استخدام Splunk ولغة SPL للتحقيق في الحوادث عبر ربط السجلات، وإعادة بناء الخط الزمني، وكشف الشذوذ (Windows/firewall/proxy/auth logs).",
        "what_en": "Use Splunk and SPL to investigate incidents via log correlation, timeline reconstruction, and anomaly detection across Windows, firewall, proxy, and auth logs.",
        "steps_ar": [
            "ابتلاع مصادر السجلات (Suricata EVE، pfSense، Windows Events)",
            "كتابة استعلامات SPL للربط والإحصاء (stats، transaction)",
            "بناء خط زمني للحادثة عبر المصادر",
            "ربط الأنماط بـ MITRE ATT&CK (brute force، pass-the-hash، RDP)",
            "إنشاء قواعد كشف ولوحات متابعة",
        ],
        "steps_en": [
            "Ingest log sources (Suricata EVE, pfSense, Windows Events)",
            "Write SPL queries for correlation and stats (stats, transaction)",
            "Build an incident timeline across sources",
            "Map patterns to MITRE ATT&CK (brute force, pass-the-hash, RDP)",
            "Create detection rules and monitoring dashboards",
        ],
        "lab_ar": "Splunk (أو بديل مفتوح مثل Wazuh) يعمل كـ VM مركزية تجمع سجلات كل أنظمة المختبر، ويمثل قلب الـ SOC المنزلي.",
        "lab_en": "Splunk (or an open alternative such as Wazuh) runs as the central VM aggregating logs from all lab systems, the heart of the home SOC.",
    },
    {
        "n": 7,
        "slug": "analyzing-dns-logs-for-exfiltration",
        "name_en": "Analyzing DNS Logs for Exfiltration",
        "name_ar": "تحليل سجلات DNS لكشف تسريب البيانات",
        "domain": "SOC Operations",
        "attack": ["T1048.003", "T1071.004", "T1567"],
        "nist": ["DE.CM-01", "DE.AE-02", "RS.MA-01", "DE.AE-06"],
        "what_ar": "تحليل استعلامات DNS لكشف تسريب البيانات عبر الأنفاق (DNS tunneling) ونطاقات DGA وقنوات C2 المخفية، باستخدام تحليل الإنتروبي وشذوذ حجم الاستعلامات.",
        "what_en": "Analyze DNS query logs to detect exfiltration via DNS tunneling, DGA domains, and covert C2 using entropy analysis, query-volume anomalies, and subdomain-length detection.",
        "steps_ar": [
            "تجميع سجلات DNS (Suricata dns event أو خادم DNS)",
            "حساب إنتروبي أسماء النطاقات لكشف DGA",
            "رصد طول النطاقات الفرعية المفرط (دليل tunneling)",
            "رصد شذوذ حجم/توقيت الاستعلامات (beaconing)",
            "إطلاق تنبيهات في الـ SIEM وربطها بـ IOCs",
        ],
        "steps_en": [
            "Collect DNS logs (Suricata dns events or the DNS server)",
            "Compute domain-name entropy to flag DGA",
            "Detect excessive subdomain length (tunneling signal)",
            "Detect query volume/timing anomalies (beaconing)",
            "Raise SIEM alerts and correlate with IOCs",
        ],
        "lab_ar": "نحاكي exfiltration داخل المختبر (مثل iodine/dnscat2) من جهاز هدف، ثم نكتشفه من سجلات DNS التي تجمعها Suricata وتحلّلها في Splunk.",
        "lab_en": "We simulate exfiltration (e.g. iodine/dnscat2) from a target VM, then detect it from the DNS logs Suricata collects and Splunk analyzes.",
    },
    {
        "n": 8,
        "slug": "building-vulnerability-scanning-workflow",
        "name_en": "Building a Vulnerability Scanning Workflow",
        "name_ar": "بناء سير عمل لفحص الثغرات",
        "domain": "Vulnerability Management",
        "attack": ["T1595.002", "T1190", "T1046"],
        "nist": ["DE.CM-01", "DE.AE-02", "RS.MA-01", "DE.AE-06"],
        "what_ar": "بناء سير عمل منظّم لفحص الثغرات بأدوات مثل OpenVAS/Nessus/Qualys لاكتشاف وترتيب وتتبع معالجة الثغرات عبر البنية التحتية.",
        "what_en": "Build a structured vulnerability scanning workflow with OpenVAS/Nessus/Qualys to discover, prioritize (beyond raw CVSS), and track remediation across infrastructure.",
        "steps_ar": [
            "جرد الأصول وتحديد نطاق الفحص",
            "جدولة فحوصات دورية (authenticated/unauthenticated)",
            "ترتيب النتائج حسب CVSS + سياق الأصل + تهديدات فعلية",
            "دمج النتائج مع تنبيهات الـ SIEM",
            "بناء لوحة تتبع المعالجة و SLA",
        ],
        "steps_en": [
            "Inventory assets and define scan scope",
            "Schedule recurring scans (authenticated/unauthenticated)",
            "Prioritize results by CVSS + asset context + real threat intel",
            "Integrate results with SIEM alerting",
            "Build a remediation-tracking and SLA dashboard",
        ],
        "lab_ar": "نشغّل OpenVAS كـ VM ونفحص أنظمة المختبر الهدف (مثل Metasploitable) لإثبات الدورة الكاملة: اكتشاف → ترتيب → معالجة → إعادة فحص.",
        "lab_en": "We run OpenVAS as a VM and scan target lab systems (e.g. Metasploitable) to demonstrate the full loop: discover → prioritize → remediate → re-scan.",
    },
    {
        "n": 9,
        "slug": "deploying-ransomware-canary-files",
        "name_en": "Deploying Ransomware Canary Files",
        "name_ar": "نشر ملفات الإنذار المبكر (Canary) ضد الفدية",
        "domain": "Ransomware Defense / Deception",
        "attack": ["T1486", "T1083", "T1490", "T1485"],
        "nist": ["PR.DS-11", "RS.MA-01", "RC.RP-01", "PR.IR-01"],
        "what_ar": "نشر ملفات خداعية (canary) تحاكي أهدافاً عالية القيمة في المجلدات، ومراقبتها لحظياً بمكتبة watchdog في Python لإطلاق تنبيه فور أي تعديل/قراءة, إنذار مبكر قبل اكتمال التشفير.",
        "what_en": "Deploy decoy \"canary\" files that mimic high-value targets, monitored in real time with Python's watchdog to alert instantly on any read/modify/rename, early warning before encryption completes.",
        "steps_ar": [
            "وضع ملفات canary بأسماء جذابة (financial_records.xlsx...) في مجلدات حساسة",
            "تشغيل مراقب watchdog لأحداث نظام الملفات",
            "تصنيف الأحداث (read/modify/rename/delete)",
            "إطلاق تنبيه (email/Slack/syslog) عند أي تفاعل",
            "ربط التنبيه بالـ SIEM وإجراء الاستجابة",
        ],
        "steps_en": [
            "Place canary files with attractive names (financial_records.xlsx…) in sensitive folders",
            "Run a watchdog monitor for filesystem events",
            "Classify events (read/modify/rename/delete)",
            "Alert (email/Slack/syslog) on any interaction",
            "Forward the alert to the SIEM and trigger response",
        ],
        "lab_ar": "ممما يميز هذه المهارة أنها هذه المهارة مبنية على Python و watchdog وتعمل مباشرة على ويندوز, أي يمكن تجربتها اليوم قبل تجهيز Proxmox، ثم نقلها لاحقاً إلى خوادم المختبر.",
        "lab_en": "Worth noting: this skill is pure Python + watchdog and runs on Windows today, you can trial it before Proxmox exists, then move it onto lab file servers later.",
    },
    {
        "n": 10,
        "slug": "analyzing-sbom-for-supply-chain-vulnerabilities",
        "name_en": "Analyzing SBOM for Supply-Chain Vulnerabilities",
        "name_ar": "تحليل SBOM لكشف ثغرات سلسلة التوريد",
        "domain": "Supply Chain Security",
        "attack": [],
        "nist": ["GV.SC-01", "GV.SC-03", "GV.SC-06", "GV.SC-07"],
        "what_ar": "تحليل قوائم مكوّنات البرمجيات (SBOM) بصيغتي CycloneDX و SPDX، ومطابقة المكوّنات مع قاعدة NVD CVE، وبناء رسم اعتماديات وحساب درجات خطورة وتقارير امتثال.",
        "what_en": "Parse SBOMs (CycloneDX/SPDX JSON), correlate components against the NVD CVE database (NVD 2.0 API), build dependency graphs, compute risk scores, and generate compliance reports.",
        "steps_ar": [
            "توليد SBOM للحاويات/التطبيقات بـ syft",
            "تحليل CycloneDX/SPDX JSON",
            "مطابقة المكوّنات مع CVEs عبر NVD 2.0 API (أو grype)",
            "بناء رسم اعتماديات ورصد المسارات المتعدية (transitive)",
            "إصدار تقرير خطورة وامتثال",
        ],
        "steps_en": [
            "Generate SBOMs for containers/apps with syft",
            "Parse CycloneDX/SPDX JSON",
            "Correlate components to CVEs via NVD 2.0 API (or grype)",
            "Build a dependency graph and surface transitive paths",
            "Produce a risk and compliance report",
        ],
        "lab_ar": "قبل نشر أي حاوية Docker داخل Ubuntu VM على Proxmox نولّد لها SBOM ونفحصه لضمان أمن سلسلة التوريد, يربط مباشرة بقسم Docker في دليل Proxmox.",
        "lab_en": "Before deploying any Docker container inside an Ubuntu VM on Proxmox, we generate and scan its SBOM to secure the supply chain, tying directly into the Docker section of the Proxmox guide.",
    },
]

# Architecture / deployment roadmap phases
ROADMAP = [
    ("المرحلة 0: قبل Proxmox (اليوم على ويندوز)",
     "Phase 0: Pre-Proxmox (today on Windows)",
     "تجربة المهارة 9 (canary files) بـ Python، وتحليل SBOM (المهارة 10) حيث لا يحتاجان hypervisor.",
     "Trial Skill 9 (canary files) in Python and Skill 10 (SBOM) since neither needs a hypervisor."),
    ("المرحلة 1: تجهيز المنصة",
     "Phase 1: Platform bring-up",
     "تثبيت Proxmox على جهاز مستقل، تأمين واجهة 8006 (المهارة 5 TLS + المهارة 4 Tailscale).",
     "Install Proxmox on a dedicated machine; secure the 8006 UI (Skill 5 TLS + Skill 4 Tailscale)."),
    ("المرحلة 2: الشبكة",
     "Phase 2: Network",
     "بناء الـ VLANs (المهارة 1) ونشر pfSense (المهارة 2) كبوّابة وعزل.",
     "Build the VLANs (Skill 1) and deploy pfSense (Skill 2) as gateway and segmentation."),
    ("المرحلة 3: المراقبة (SOC)",
     "Phase 3: Monitoring (SOC)",
     "نشر Suricata (المهارة 3) و Splunk/Wazuh (المهارة 6)، ثم كشف DNS (المهارة 7).",
     "Deploy Suricata (Skill 3) and Splunk/Wazuh (Skill 6), then DNS detection (Skill 7)."),
    ("المرحلة 4: الاختبار والتصليب",
     "Phase 4: Test & harden",
     "تشغيل فحص الثغرات (المهارة 8)، محاكاة هجمات داخل المختبر ورصدها في الـ SOC.",
     "Run vulnerability scans (Skill 8), simulate in-lab attacks and observe them in the SOC."),
]


# ---- Tier 2: executed inside the real Proxmox VE 9.2.2 node (192.168.29.132) ----
AGENT_RUNS += [
    {
        "skill": "configuring-network-segmentation-with-vlans",
        "cmd": "ssh root@192.168.29.132 -> /etc/network/interfaces + ifreload -a",
        "evidence": "evidence/08_vlan_segmentation_agent.txt",
        "result_ar": (
            "قسّمنا الشبكة داخل العقدة إلى ثلاث مناطق منفصلة: vmbr10 لشبكة الخوادم على 10.10.10.0/24، و vmbr20 لأنظمة "
            "الهدف على 10.10.20.0/24، و vmbr30 لأدوات المراقبة على 10.10.30.0/24. ثم حوّلنا الجسر الأساسي vmbr0 إلى وصلة "
            "trunk موسومة بمعيار 802.1Q. أظهر التحقق أن القيمة vlan_filtering أصبحت 1 وأن جدول الـ VLAN فعّال، دون أن "
            "ينقطع الاتصال بالعقدة أثناء التطبيق. لم تنجح المحاولة الأولى في الواقع، إذ كتب أمر sed المُعامل بصيغة مشوّهة "
            "فرفضها النظام، فأعدنا كتابته وطبّقناه من جديد."
        ),
        "result_en": (
            "We split the network inside the node into three separate zones: vmbr10 for servers on 10.10.10.0/24, vmbr20 "
            "for target systems on 10.10.20.0/24, and vmbr30 for monitoring tools on 10.10.30.0/24. The main bridge, "
            "vmbr0, was then converted into an 802.1Q tagged trunk. Checking afterwards showed vlan_filtering set to 1 "
            "with an active VLAN table, and connectivity to the node held throughout. The first attempt did not actually "
            "work: sed wrote the directive in a malformed way and the system rejected it, so we rewrote and reapplied it."
        ),
    },
    {
        "skill": "configuring-suricata-for-network-monitoring",
        "cmd": "apt install suricata; custom lab.rules; attack simulation",
        "evidence": "evidence/09_suricata_agent.txt",
        "result_ar": (
            "ثبّتنا Suricata بإصدار 7.0.10 وكتبنا خمس قواعد كشف خاصة بالمختبر، ربطنا كلاً منها بتقنية من MITRE ATT&CK. "
            "بعد تشغيل الخدمة ولّدنا مروراً هجومياً داخل المختبر لاختبارها، فسجّلت ستة تنبيهات فعلية ظهرت في ملفي "
            "fast.log و eve.json: تنبيه لمسح ICMP يقابل T1018، وأربعة تنبيهات لأنماط تسريب عبر DNS تقابل T1048.003، "
            "وتنبيه لمسح منافذ يقابل T1046. قاعدتان من الخمس لم تُطلقا: قاعدة User-Agent الخاصة بقنوات التحكم، لأن مسار "
            "الاختبار لم يكن فيه خادم HTTP يستقبل الطلب، وقاعدة نفق DNS لأن الاستعلام الطويل لم يطابق نمط pcre الذي "
            "كتبناه."
        ),
        "result_en": (
            "Suricata 7.0.10 was installed together with five lab-specific detection rules, each tied to a MITRE ATT&CK "
            "technique. Once the service was running we generated attack traffic inside the lab to test them, and six "
            "real alerts were logged in fast.log and eve.json: an ICMP sweep matching T1018, four DNS exfiltration "
            "patterns matching T1048.003, and a port scan matching T1046. Two of the five rules stayed silent. The C2 "
            "User-Agent rule never fired because there was no HTTP server on the test path to receive the request, and "
            "the DNS tunnelling rule missed because the long query did not match the pcre pattern we had written."
        ),
    },
    {
        "skill": "analyzing-dns-logs-for-exfiltration (real data)",
        "cmd": "jq (Suricata EVE dns events) | python run_dns_on_real.py",
        "evidence": "evidence/11_dns_agent_on_real_suricata_data.txt",
        "result_ar": (
            "هذه أقوى نتيجة في المشروع. أخرجنا 36 حدث DNS حقيقياً كانت Suricata قد التقطتها من العقدة، ومرّرناها إلى وكيل "
            "تحليل سجلات DNS. رصد الوكيل نفقين اثنين: النطاق test.localdomain بثمانية استعلامات ومتوسط طول 72 حرفاً "
            "للنطاق الفرعي، والنطاق evil-tunnel.test بستة استعلامات ومتوسط طول 60. أهمية هذه النتيجة أنها تُثبت سلسلة كشف "
            "مكتملة من طرف إلى طرف: هجوم جرى فعلاً، التقطته أداة مراقبة حقيقية، حلّله وكيل مستقل، فخرج بكشف صحيح."
        ),
        "result_en": (
            "This is the strongest result in the project. We extracted 36 real DNS events that Suricata had captured on "
            "the node and passed them to the DNS log analysis agent. It picked out two tunnels: test.localdomain, with "
            "eight queries averaging 72 characters of subdomain, and evil-tunnel.test, with six queries averaging 60. "
            "What matters here is that this demonstrates a complete end-to-end detection chain: an attack that genuinely "
            "happened, captured by a real monitoring tool, analysed by a separate agent, and correctly identified."
        ),
    },
    {
        "skill": "configuring-pfsense-firewall-rules (adapted)",
        "cmd": "/etc/pve/firewall/cluster.fw ; pve-firewall compile && restart",
        "evidence": "evidence/12_firewall_agent.txt",
        "result_ar": (
            "يتطلب pfSense جهازاً افتراضياً مستقلاً بواجهتي شبكة، وهو ما لم تسمح به موارد المختبر، فنفّذنا السياسة نفسها "
            "باستخدام الجدار الناري المدمج في Proxmox. اعتمدنا مبدأ المنع الافتراضي لكل الوارد، وعرّفنا أسماء مستعارة لكل "
            "منطقة شبكية، ثم سمحنا لشبكة الإدارة وحدها بالوصول إلى المنفذين 8006 و22 مع تسجيل هذه المحاولات، ومنعنا شبكة "
            "الأهداف من بلوغ شبكتي الإدارة والخوادم لقطع أي حركة جانبية. تحقّقنا من ذلك بقراءة قواعد iptables الفعلية في "
            "النواة. أخطأنا في المحاولة الأولى حين استخدمنا البادئة +dc/ وهي مخصّصة لمجموعات IPSet لا للأسماء المستعارة. "
            "ولأن سياسة المنع الافتراضي قد تقطع الوصول عن المسؤول نفسه، شغّلنا آلية تراجع تلقائي قبل تفعيل السياسة "
            "تحسّباً لذلك."
        ),
        "result_en": (
            "pfSense needs its own virtual machine with two network interfaces, which the lab's resources did not allow, "
            "so we implemented the same policy using the firewall built into Proxmox. We applied default-deny on all "
            "inbound traffic, defined aliases for each network zone, then allowed only the management network to reach "
            "ports 8006 and 22 while logging those attempts, and blocked the targets network from reaching management and "
            "servers so lateral movement had nowhere to go. This was confirmed by reading the actual iptables rules in "
            "the kernel. We got the first attempt wrong by using the +dc/ prefix, which belongs to IPSets rather than "
            "aliases. Because a default-deny policy can lock out the administrator, an automatic rollback was armed "
            "before the policy went live as a precaution."
        ),
    },
    {
        "skill": "analyzing-security-logs-with-splunk (adapted)",
        "cmd": "collect Suricata EVE + sshd journal -> correlation engine",
        "evidence": "evidence/13_siem_correlation_agent.txt",
        "result_ar": (
            "Splunk Enterprise يحتاج خادماً مرخّصاً غير متاح لنا، فطبّقنا منطق الارتباط ذاته الذي تصفه المهارة على بيانات "
            "المختبر الحقيقية. جمعنا 26 حدثاً من مصدرين هما Suricata وسجل sshd، وأجرينا عليها الإحصاء وإعادة بناء الخط "
            "الزمني وربط الأنماط بالتقنيات. أعاد التحليل ترتيب الحادثة زمنياً، وحدّد المضيف الأكثر نشاطاً، وأظهر تغطية "
            "شملت T1048.003 بأربعة رصدات و T1018 و T1046 برصدة لكل منهما. الخلاصة التحليلية أن مضيفاً داخلياً واحداً أنتج "
            "استطلاعاً ومحاولة تسريب خلال اثنتي عشرة ثانية، وهو إيقاع يدل على أداة آلية لا على نشاط بشري."
        ),
        "result_en": (
            "Splunk Enterprise requires a licensed server we did not have, so we applied the same correlation logic the "
            "skill describes to the lab's real data. We collected 26 events from two sources, Suricata and the sshd "
            "journal, then ran statistics, timeline reconstruction and technique mapping over them. The analysis put the "
            "incident back in chronological order, identified the busiest host, and showed coverage spanning T1048.003 "
            "with four detections plus T1018 and T1046 with one each. The analytical conclusion was that a single "
            "internal host produced reconnaissance and an exfiltration attempt within twelve seconds, a tempo that points "
            "to automated tooling rather than a human operator."
        ),
    },
    {
        "skill": "building-vulnerability-scanning-workflow",
        "cmd": "nmap -sn / -sV --top-ports 200 ; apt-get -s upgrade",
        "evidence": "evidence/10_vulnerability_scanning_agent.txt",
        "result_ar": (
            "اقتصر الفحص على أصول المختبر التي نملكها. عثرنا على أربعة مضيفات نشطة، وعدّدنا الخدمات المكشوفة على العقدة "
            "فوجدنا خدمة SSH بإصدار OpenSSH 10.0p2، وخادم بريد Postfix، وخدمة rpcbind، وواجهة Proxmox البرمجية. كما تبيّن "
            "أن 61 حزمة تنتظر التحديث، وهي نتيجة ذات دلالة أمنية مباشرة. رتّبنا النتائج في جدول بحسب الخطورة، وأرفقنا مع "
            "كل بند إجراء المعالجة المقترح."
        ),
        "result_en": (
            "The scan was limited to lab assets we own. We found four live hosts and enumerated the services exposed on "
            "the node: SSH running OpenSSH 10.0p2, a Postfix mail server, rpcbind, and the Proxmox API interface. It also "
            "emerged that 61 packages were awaiting updates, a finding with direct security significance. The results "
            "were arranged in a table ordered by severity, each entry paired with a suggested remediation."
        ),
    },
    {
        "skill": "configuring-tls-1-3 (live Proxmox UI)",
        "cmd": "agent.py --host 192.168.29.132 --port 8006",
        "evidence": "evidence/07_tls_agent_vs_proxmox.txt, evidence/tls_pve_node.json",
        "result_ar": (
            "شغّلنا وكيل تدقيق TLS على واجهة إدارة Proxmox الحيّة. جاءت النتيجة مطمئنة في معظمها: الإصداران القديمان TLS "
            "1.0 و1.1 معطّلان، والإصداران 1.2 و1.3 مدعومان، وتم التفاوض على مجموعة التشفير TLS_AES_256_GCM_SHA384 عبر TLS "
            "1.3. لكن الشهادة ذاتية التوقيع صادرة عن سلطة PVE Cluster Manager الداخلية بمفتاح طوله 2048 بت وصلاحية 728 "
            "يوماً، وهذه بالتحديد هي الملاحظة التي بُنيت عليها توصيتنا بنشر شهادة موثوقة بدلاً منها."
        ),
        "result_en": (
            "We ran the TLS audit agent against the live Proxmox management interface. Most of what came back was "
            "reassuring: the older TLS 1.0 and 1.1 are disabled, 1.2 and 1.3 are supported, and the connection negotiated "
            "TLS_AES_256_GCM_SHA384 over TLS 1.3. The certificate, however, is self-signed by the internal PVE Cluster "
            "Manager authority with a 2048-bit key valid for 728 days, and that is precisely the observation behind our "
            "recommendation to deploy a trusted certificate in its place."
        ),
    },
    {
        "skill": "deploying-tailscale-for-zero-trust-vpn",
        "cmd": "apt install tailscale (official signed repo); sysctl ip_forward",
        "evidence": "evidence/14_tailscale_agent.txt",
        "result_ar": (
            "ثبّتنا Tailscale بإصدار 1.98.10 من مستودعه الرسمي الموقّع، وتعمل خدمة tailscaled، ووحدة WireGuard محمّلة في "
            "النواة، وفعّلنا إعادة توجيه الحزم استعداداً لدور subnet router. تبقّت خطوة واحدة لم تُنفَّذ: الأمر tailscale "
            "up يتطلب تسجيل دخول بحساب المشغّل لدى مزوّد الهوية، وهو حساب شخصي، فتُركت هذه الخطوة لصاحب المشروع وتُنفَّذ "
            "بأمر واحد عند الحاجة."
        ),
        "result_en": (
            "Tailscale 1.98.10 was installed from its official signed repository. The tailscaled service is running, the "
            "WireGuard kernel module is loaded, and packet forwarding was enabled ready for the subnet-router role. One "
            "step remains unfinished: the tailscale up command needs a login with the operator's identity-provider "
            "account, which is a personal account, so that step was left to the project owner and takes a single command "
            "whenever it is wanted."
        ),
    },
]

# Lab build facts table (verified)
LAB_FACTS = [
    ("Hypervisor", "VMware Workstation 25 (nested virtualization enabled)"),
    ("Guest platform", "Proxmox VE 9.2.2 on kernel 7.0.2-6-pve"),
    ("ISO integrity", "SHA-256 verified against proxmox.com (4e88fe41…f2c6c)"),
    ("Node resources", "4 vCPU (i7-12700), 6 GB RAM, 80 GB disk"),
    ("Nested KVM", "/dev/kvm present, so VMs can run inside the node"),
    ("Management URL", "https://192.168.29.132:8006"),
    ("Agent access", "ed25519 SSH key (password auth not used)"),
    ("Zones created", "vmbr10 servers / vmbr20 targets / vmbr30 monitoring"),
    ("802.1Q trunk", "vmbr0 vlan_filtering = 1"),
    ("Firewall", "pve-firewall active, deny-by-default, iptables verified"),
    ("IDS", "Suricata 7.0.10, 5 custom rules, 6 real alerts captured"),
    ("ZTNA", "Tailscale 1.98.10 installed; activation pending user login"),
]
