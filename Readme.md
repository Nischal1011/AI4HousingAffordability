# Housing Affordability and Section 8 Research Project

## Table of Contents
1. [Project Overview](#project-overview)
2. [Housing Shortage Heatmap](#housing-shortage-heatmap)
3. [Affordability Index](#affordability-index)
4. [Neighborhood Stability Index](#neighborhood-stability-index)
5. [Dynamic Pricing & Forecasting](#dynamic-pricing--forecasting)
6. [Explainable AI for Housing](#explainable-ai-for-housing)
7. [Data Processing Tools](#data-processing-tools)

## Project Overview
This comprehensive research project addresses critical issues in the housing sector, with a specific focus on Section 8 housing and affordable housing challenges. Through multiple interconnected sub-projects, we aim to:
- Identify housing shortages
- Create affordability indices
- Forecast rental price trends
- Ensure fair and transparent AI-driven housing recommendations

## Housing Shortage Heatmap
### Objective
Identify areas where Section 8 housing demand exceeds supply to guide resource allocation.

### Data Sources
- Census.gov data
- HUD datasets
- Geospatial tools (Folium, Plotly, ArcGIS)

### Expected Impact
- Guide policymakers in identifying underserved areas
- Enable effective resource allocation by local governments
- Support data-driven housing development decisions

## Affordability Index
### Objective
Create a comprehensive index measuring housing affordability based on key economic indicators.

### Key Components
- Mortgage rates
- Household income levels
- Rent levels
- Housing cost burden analysis

### Data Sources
- Freddie Mac/FRED mortgage data
- Census Bureau statistics
- HUD affordable housing data

## Neighborhood Stability Index
### Objective
Provide data-driven insights on neighborhood livability and long-term stability.

### Key Metrics
- Crime rates
- School quality
- Transportation access
- Employment trends

### Data Sources
- FBI UCR Crime Reports
- National Center for Education Statistics
- Bureau of Labor Statistics
- Google Maps API/OpenStreetMap

## Dynamic Pricing & Forecasting
### Objective
Predict future rental price trends for Section 8 housing.

### Methodology
- Time-series forecasting (ARIMA, Prophet)
- Economic indicator analysis
- Policy impact assessment

### Data Sources
- HUD rental data
- Federal Reserve statistics
- Zillow Research data

## Explainable AI for Housing
### Objective
Develop unbiased, interpretable AI-driven housing recommendations.

### Technical Approach
- SHAP (Shapley Additive Explanations)
- LIME (Local Interpretable Model-Agnostic Explanations)
- Fairness metrics implementation

### Expected Outcomes
- Transparent recommendation systems
- Reduced algorithmic bias
- Improved trust in AI-driven solutions

## Data Processing Tools
This repository includes Python tools for processing HUD data and generating key metrics:

### Features
- Data cleaning and standardization
- Metric calculation
- Geospatial analysis
- Statistical modeling

### Requirements
- Python 3.x
- pandas
- numpy
- Additional requirements in `requirements.txt`

### Installation
```bash
git clone [repository-url]
pip install -r requirements.txt
```

### Usage
```bash
python HUD.py
```

