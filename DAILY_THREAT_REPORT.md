# Daily Automated Threat Intelligence Report
*Generated on: 2026-07-17 10:07:29 (UTC)*

### [The Hacker News] CISA Adds Exploited SharePoint RCE Zero-Day CVE-2026-58644 to KEV
- **Link:** https://thehackernews.com/2026/07/cisa-adds-exploited-sharepoint-rce-zero.html
- **AI Analysis:**
> Okay, let's break down this security news.

**Severity:** Critical

**1-Sentence Impact:** This critical, actively exploited SharePoint RCE vulnerability (CVE-2026-58644) enables attackers to achieve full system compromise, posing an immediate and severe risk to organizations using unpatched SharePoint Servers.

---

**Reasoning for Severity:**

1.  **Exploited in the Wild:** The most crucial factor. CISA adding it to the KEV catalog explicitly means it's being actively exploited. This elevates any vulnerability, especially one of this type, to critical status.
2.  **RCE (Remote Code Execution):** This is the most severe type of vulnerability, allowing an attacker to run arbitrary code on the affected server. This typically leads to full system compromise, data theft, or further network penetration.
3.  **CVSS Score: 9.8 (Critical):** The CVSS score directly indicates critical severity according to industry standards.
4.  **Affected Software: Microsoft SharePoint Server:** SharePoint is widely used by enterprises and government agencies, often storing highly sensitive information, making a compromise particularly damaging.
5.  **CISA KEV Mandate:** The requirement for FCEB agencies to patch highlights the immediate and serious threat perceived by a top cybersecurity agency.
6.  **"Zero-Day" (implied from title):** While the summary says "newly patched," the title mentioning "Zero-Day" implies it was exploited before a patch was generally available, indicating sophisticated attackers and potentially broader initial compromise.
7.  **"Critical deserialization":** Deserialization vulnerabilities are a common and powerful vector for achieving RCE.

**Note on the Date:** There appears to be a typo in the provided text. A CVE year of "2026" and a remediation deadline of "July 19, 2026" for a "newly patched" and "zero-day" vulnerability added to KEV *now* doesn't make sense. It's highly probable the CVE is CVE-2024-58644 (or similar for 2024) and the deadline is July 19, **2024**. However, even with this potential typo, the *facts* of RCE, KEV listing, active exploitation, and high CVSS firmly establish its critical severity.

---

### [The Hacker News] Two Scattered Spider Hackers Get 5.5 Years Each for £29 Million TfL Hack
- **Link:** https://thehackernews.com/2026/07/two-scattered-spider-hackers-get-55.html
- **AI Analysis:**
> **Severity:** Critical

**Impact:** This attack resulted in a massive £29 million financial loss and severe operational disruption, incapacitating 148 critical systems and forcing 27,000 employees into a manual password reset for Transport for London.

---

### [The Hacker News] ThreatsDay: Game Cheat Spyware, 24-Hour Ransomware, Chrome Sync Stalking + 12 More Stories
- **Link:** https://thehackernews.com/2026/07/threatsday-game-cheat-spyware-24-hour.html
- **AI Analysis:**
> **Severity:** Critical

**1-sentence Impact:** Widespread threats, including rapid ransomware attacks, data-stealing spyware, and privacy violations, pose critical risks of significant financial loss and system compromise through deceptive methods and exploitable weaknesses.

---

### [The Hacker News] n8n Token Exchange Flaw Could Let Attackers Log In as Users From Another Issuer
- **Link:** https://thehackernews.com/2026/07/n8n-token-exchange-flaw-could-let.html
- **AI Analysis:**
> **Severity:** Critical

**Impact:** Attackers can bypass authentication to impersonate any user on multi-issuer configured Enterprise instances, gaining full access to their accounts and all associated data and workflows.

---

### [The Hacker News] New TELEPUZ Malware Spreads via ClickFix to Steal Data and Run Commands
- **Link:** https://thehackernews.com/2026/07/new-telepuz-malware-spreads-via.html
- **AI Analysis:**
> **Severity:** High

**Impact:** The new TELEPUZ modular malware poses a high risk of sensitive data theft and full system compromise due to its remote command execution capabilities.

---

### [Bleeping Computer] Windows Server 2022 reach end of mainstream support in 90 days
- **Link:** https://www.bleepingcomputer.com/news/microsoft/windows-server-2022-reach-end-of-mainstream-support-in-90-days/
- **AI Analysis:**
> This news indicates a standard product lifecycle announcement rather than an immediate security vulnerability.

*   **Severity:** **Low**
*   **Impact:** While Windows Server 2022 will cease receiving new features and non-security fixes, it will continue to receive critical security updates under extended support until October 2031, providing ample time for organizations to plan future migrations.

---

### [Bleeping Computer] US charges two over laundering $43 million from investment fraud
- **Link:** https://www.bleepingcomputer.com/news/security/us-charges-two-over-laundering-43-million-from-investment-fraud/
- **AI Analysis:**
> Analysis failed: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 34.881726713s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 34
}
]

---

### [Bleeping Computer] CISA urges immediate action on actively exploited Fortinet flaws
- **Link:** https://www.bleepingcomputer.com/news/security/cisa-warns-feds-to-patch-exploited-fortinet-fortisandbox-flaws-by-sunday/
- **AI Analysis:**
> Analysis failed: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 33.788802897s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 33
}
]

---

### [Bleeping Computer] New ClickLock macOS malware traps users into revealing login password
- **Link:** https://www.bleepingcomputer.com/news/security/new-clicklock-macos-malware-traps-users-into-revealing-login-password/
- **AI Analysis:**
> Analysis failed: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 32.694900115s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 32
}
]

---

### [Bleeping Computer] Coca-Cola says Fairlife ransomware attack halts US dairy production
- **Link:** https://www.bleepingcomputer.com/news/security/coca-cola-says-fairlife-ransomware-attack-halts-us-dairy-production/
- **AI Analysis:**
> Analysis failed: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 31.608818186s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 31
}
]

---

