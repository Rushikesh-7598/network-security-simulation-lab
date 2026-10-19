# Testing guide

## 1. Test the one-click dashboard
1. Run `RUN_WINDOWS.bat` or `bash RUN_MAC_LINUX.sh`.
2. Confirm the dashboard opens at `http://127.0.0.1:8765/index.html`.
3. Click **Run all tests**. The included scenarios should pass against the embedded policy model.
4. Try different source, destination, and protocol choices in **Test a connection**.
5. Load sample events and filter security-relevant rows.
6. Download the JSON report and inspect its `mode` and `note` fields.

## 2. What the dashboard tests
It tests a deterministic policy model:
- Employee -> server HTTPS: allow
- Employee -> server SSH: deny
- Employee -> Admin: deny
- Admin -> server SSH: allow
- Server -> Admin: deny
- Employee -> external HTTPS: allow

These are model-level tests only. They are not proof that real ACLs, firewalls, or IDS rules work.

## 3. Real implementation path
To perform hands-on networking tests, use Cisco Packet Tracer or a suitable network emulator to implement the reference configurations. For real packet capture and Suricata alerts, create an isolated VM lab, configure a monitoring interface, generate only controlled lab traffic, and save screenshots/logs under `reports/` or a separate evidence folder.

## 4. Safety
Do not apply sample configs to production equipment. Do not capture traffic on networks without authorization. Keep virtual machines on host-only/internal networks unless you have a clear need and permission to connect them elsewhere.
