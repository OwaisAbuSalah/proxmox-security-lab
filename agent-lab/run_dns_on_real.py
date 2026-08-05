import json, sys, importlib.util
spec = importlib.util.spec_from_file_location("dnsagent",
    "skills/analyzing-dns-logs-for-exfiltration/scripts/agent.py")
m = importlib.util.module_from_spec(spec)
sys.argv=["agent"]
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):   # suppress its demo block
    spec.loader.exec_module(m)

records=[json.loads(l) for l in open("evidence/real_dns_events.json",encoding="utf-8") if l.strip()]
print(f"Loaded {len(records)} REAL DNS query events captured by Suricata on the Proxmox node\n")

print("--- [1] DNS Tunneling Detection (T1071.004) ---")
for t in m.detect_tunneling(records, subdomain_len_threshold=30, min_queries=3):
    print(f"  [ALERT] {t['domain']}: {t['queries']} queries | "
          f"avg subdomain len={t['avg_subdomain_length']} | sources={t.get('source_ips',t.get('sources'))}")

print("\n--- [2] DGA Detection (entropy) ---")
d=m.detect_dga(records, entropy_threshold=3.0, min_sld_length=8)
print("  [none]" if not d else "")
for x in d[:5]: print(f"  [ALERT] {x['domain']}: entropy={x['avg_entropy']}")

print("\n--- [3] Entropy of observed domains ---")
seen=[]
for r in records:
    q=r["query"].split(".")[0]
    if q not in seen:
        seen.append(q)
for q in seen[:6]:
    print(f"  '{q[:42]}{'...' if len(q)>42 else ''}' -> entropy={m.shannon_entropy(q)}")
