# Aqua-Insight

Aqua Insight is an IoT and AI-based smart water management system that uses sensors for predictive NRW loss by Leaks and Contamination. This system aims for:

## 1. NON-REVENUE WATER (NRW) LOSS REDUCTION
*   **IoT Monitoring:** Deploy LoRaWAN/NB-IoT Sensors (Flow, Pressure, Quality) to establish District Metered Areas (DMAs). This pinpoints the source of physical leakage instantly.
*   **Predictive AI:** Use Machine Learning (ML) on DMA data to predict pipeline bursts before they occur, enabling proactive maintenance.
*   **Supply Integrity:** Real-time TDS/Turbidity Sensors ensure continuous water quality monitoring, reducing wastage on contamination risk.

## 2. AWARENESS IN WATER CONSERVATION
*   **Citizen Engagement App:** The AquaCitizen App provides personalized water consumption and conservation scores based on IoT usage data.
*   **Wastage Reporting:** The app serves as a centralized communication hub for citizens to instantly report public water wastage and leaks.

## 3. WASTEWATER TREATMENT & REUSE
*   **Decentralized Reuse Hardware:** Introduce the 'Jal-Mitra' Graywater Kit—a low-cost, household filtration/UV unit built on the ESP32 platform.
*   **Automated Segregation:** The kit manages the mandatory 3-way segregation (Plants/Flush/Central Line) at the source, treating and diverting water for immediate, non-potable domestic reuse.
*   **Holistic Management:** The system integrates data from all points to achieve full water cycle transparency for KRWSA.

---

## Technologies Used

### Sensors
*   Water flow sensor
*   pH sensor
*   Turbidity sensor
*   Total Dissolved Solid (TDS) sensor
    *   *Note: All these ensure real-time water flow traceability.*

### Hardware
*   **ESP32:** Microcontroller with built-in Wi-Fi for direct cloud connectivity.
*   Arduino IDE
*   Arduino Cloud

### Application
*   Django
*   Python
*   Firebase

---

## Google Technologies Used
*   **Google Cloud Platform (GCP):** For scalable cloud infrastructure.
*   **Google Firebase:** For real-time database, authentication, and notifications.
*   **Google Maps Platform:** For GIS mapping, location tracking, and visualization.
*   **Google Cloud IoT (or Pub/Sub):** For secure IoT data ingestion and device communication.
*   **Google BigQuery:** For large-scale data analytics and pattern detection.
*   **Google Cloud AI / ML Tools:** For predictive analytics and anomaly detection.
*   **Google App Engine / Cloud Functions:** For backend services and automation.

---

## Architecture
<img width="1006" height="291" alt="image" src="https://github.com/user-attachments/assets/cf4c2ff1-0dc1-41a4-8d0d-e13fa83dff0b" />
<img width="1374" height="460" alt="image" src="https://github.com/user-attachments/assets/f6432fb8-6cc5-4300-8c96-35170770ec49" />
<img width="1464" height="324" alt="image" src="https://github.com/user-attachments/assets/8f804383-ef41-4ee7-b4d3-a60964f7ddf2" />

