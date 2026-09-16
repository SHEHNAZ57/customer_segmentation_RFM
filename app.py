import streamlit as st
import pandas as pd
import altair as alt


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Customer Intelligence",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PREMIUM VISUAL DESIGN
# ============================================================

st.html("""
<style>

    /* --------------------------------------------------------
       GLOBAL
    -------------------------------------------------------- */

    .stApp {
        background: #F5F3EE;
        color: #142A36;
    }

    .main {
        background: #F5F3EE;
    }

    .block-container {
        max-width: 1450px;
        padding-top: 2.2rem;
        padding-bottom: 3rem;
    }

    /* Main typography */

    h1, h2, h3 {
        color: #122735 !important;
        letter-spacing: -0.025em;
    }

    h1 {
        font-size: 3rem !important;
        font-weight: 650 !important;
    }

    h2 {
        font-size: 2rem !important;
        font-weight: 600 !important;
    }

    h3 {
        font-size: 1.25rem !important;
        font-weight: 600 !important;
    }

    p {
        color: #60727A;
    }


    /* --------------------------------------------------------
       SIDEBAR
    -------------------------------------------------------- */

    [data-testid="stSidebar"] {
        background: #12363A;
        border-right: 1px solid #24494D;
    }

    [data-testid="stSidebar"] * {
        color: #F4F5F0;
    }

    /* Selected sidebar radio button */

    [data-testid="stSidebar"] [data-testid="stRadio"] input[type="radio"]:checked + div {
        background: #B0884D !important;
        background-color: #B0884D !important;
        border-color: #B0884D !important;
    }

    [data-testid="stSidebar"] [data-testid="stRadio"] input[type="radio"]:checked + div > div {
        background: #B0884D !important;
        background-color: #B0884D !important;
    }

    [data-testid="stSidebar"] .stRadio label {
        color: #E6ECEA !important;
        font-size: 0.98rem;
    }

    [data-testid="stSidebar"] .stRadio > div {
        gap: 0.35rem;
    }

    [data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.16);
    }

    /* Sidebar radio selected state */

    [data-testid="stSidebar"] [role="radiogroup"] label {
        border-radius: 10px;
        padding: 0.45rem 0.6rem;
        transition: 0.2s ease;
    }

    [data-testid="stSidebar"] [role="radiogroup"] label:hover {
        background: rgba(255,255,255,0.08);
    }


    /* --------------------------------------------------------
       CUSTOM SECTION LABELS
    -------------------------------------------------------- */

    .eyebrow {
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.20em;
        text-transform: uppercase;
        color: #B0884D;
        margin-bottom: 0.45rem;
    }

    .sidebar-brand {
        font-size: 1.22rem;
        font-weight: 700;
        letter-spacing: 0.03em;
        color: #FFFFFF;
        margin-top: 0.3rem;
    }

    .sidebar-subtitle {
        color: #B8C9C8;
        font-size: 0.82rem;
        line-height: 1.5;
        margin-top: 0.35rem;
    }

    .sidebar-section {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: #D4B06B;
        margin-top: 1.2rem;
        margin-bottom: 0.45rem;
    }

    .sidebar-footer {
        color: #A9BFBD;
        font-size: 0.75rem;
        line-height: 1.5;
        margin-top: 1rem;
    }


    /* --------------------------------------------------------
       HERO
    -------------------------------------------------------- */

    .hero-subtitle {
        color: #65777E;
        font-size: 1.02rem;
        margin-top: -0.7rem;
        margin-bottom: 1.5rem;
    }


    /* --------------------------------------------------------
       CARDS
    -------------------------------------------------------- */

    [data-testid="stVerticalBlockBorderWrapper"] {
        border-color: #DDDCD5 !important;
        border-radius: 16px !important;
        background: #FCFBF8 !important;
        box-shadow: 0 5px 20px rgba(18, 42, 55, 0.045);
    }

    .soft-card {
        background: #F8FAF8;
        border: 1px solid #D9E2DF;
        border-radius: 16px;
        padding: 1.25rem 1.35rem;
    }

    .gold-card {
        background: #FBF7ED;
        border: 1px solid #E6D8B8;
        border-radius: 16px;
        padding: 1.25rem 1.35rem;
    }

    .blue-card {
        background: #F1F6F8;
        border: 1px solid #D5E2E7;
        border-radius: 16px;
        padding: 1.25rem 1.35rem;
    }

    .green-card {
        background: #F1F7F3;
        border: 1px solid #D3E3D9;
        border-radius: 16px;
        padding: 1.25rem 1.35rem;
    }

    .purple-card {
        background: #F6F2F9;
        border: 1px solid #E1D5E8;
        border-radius: 16px;
        padding: 1.25rem 1.35rem;
    }


    /* --------------------------------------------------------
       METRICS
    -------------------------------------------------------- */

    [data-testid="stMetric"] {
        background: #FCFBF8;
        border: 1px solid #DDDCD5;
        border-radius: 14px;
        padding: 1rem 1.1rem;
        box-shadow: 0 4px 16px rgba(18, 42, 55, 0.035);
    }

    [data-testid="stMetricLabel"] {
        color: #6B7D83 !important;
        font-size: 0.72rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }

    [data-testid="stMetricValue"] {
        color: #142A36 !important;
        font-size: 1.55rem !important;
        font-weight: 650 !important;
    }


    /* --------------------------------------------------------
       SELECTBOX
    -------------------------------------------------------- */

    div[data-baseweb="select"] > div {
        background: #FCFBF8;
        border-color: #D8D8D2;
        border-radius: 10px;
    }


    /* --------------------------------------------------------
       DATAFRAME
    -------------------------------------------------------- */

    [data-testid="stDataFrame"] {
        border: 1px solid #DDDCD5;
        border-radius: 14px;
        overflow: hidden;
    }


    /* --------------------------------------------------------
       BUTTONS / SMALL ELEMENTS
    -------------------------------------------------------- */

    .stButton button {
        border-radius: 9px;
        border: 1px solid #D5D5CE;
        background: #FCFBF8;
        color: #17343B;
    }

    .stButton button:hover {
        border-color: #B0884D;
        color: #17343B;
    }


    /* --------------------------------------------------------
       FOOTER
    -------------------------------------------------------- */

    .footer {
        text-align: center;
        color: #89969A;
        font-size: 0.72rem;
        padding-top: 2.5rem;
        padding-bottom: 1rem;
        letter-spacing: 0.04em;
    }

</style>
""")


# ============================================================
# DATA
# ============================================================

@st.cache_data
def load_data():
    df = pd.read_csv("final_customer_segments.csv")

    df["CustomerID"] = df["CustomerID"].astype(int)

    return df


df = load_data()


# ============================================================
# SEGMENT ORDER
# ============================================================

segment_order = [
    "High-Value Engaged",
    "Moderate / Regular",
    "Recent / Low-Frequency",
    "Inactive / Low-Value"
]

df["Segment"] = pd.Categorical(
    df["Segment"],
    categories=segment_order,
    ordered=True
)


# ============================================================
# SEGMENT SUMMARY
# ============================================================

segment_summary = (
    df.groupby("Segment", observed=True)
    .agg(
        Customers=("CustomerID", "count"),
        Purchase_Value=("Monetary", "sum"),
        Avg_Recency=("Recency", "mean"),
        Avg_Frequency=("Frequency", "mean"),
        Avg_Monetary=("Monetary", "mean")
    )
    .reset_index()
)

total_customers = len(df)
total_purchase_value = df["Monetary"].sum()

segment_summary["Customer_Share"] = (
    segment_summary["Customers"] / total_customers * 100
)

segment_summary["Value_Share"] = (
    segment_summary["Purchase_Value"] / total_purchase_value * 100
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.html("""
<div style="
    display:flex;
    align-items:flex-start;
    gap:11px;
    margin-bottom:6px;
">
    <div style="
        font-size:1.35rem;
        line-height:1.1;
        color:#E8D3A1;
        padding-top:2px;
    ">
        ◆
    </div>

    <div>
        <div style="
            font-size:1.18rem;
            font-weight:700;
            letter-spacing:0.10em;
            color:#FFFFFF;
            line-height:1.15;
        ">
            RFM ANALYTICS
        </div>

        <div style="
            font-size:0.72rem;
            font-weight:500;
            letter-spacing:0.08em;
            color:#B8C9C8;
            margin-top:5px;
        ">
            CUSTOMER INTELLIGENCE
        </div>
    </div>
</div>
""")

    st.divider()

    st.markdown(
        '<div class="sidebar-section">Navigation</div>',
        unsafe_allow_html=True
    )

    page = st.radio(
        "",
        [
            "Overview",
            "Customers",
            "Segments",
            "Insights"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown(
        '<div class="sidebar-section">Analytics Engine</div>',
        unsafe_allow_html=True
    )

    st.markdown("RFM Analysis")
    st.markdown("K-Means Clustering")


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    '<div class="eyebrow", text-align:"center">Customer Intelligence</div>',
    unsafe_allow_html=True
)

if page == "Overview":
    st.title("Customer Intelligence")
    st.markdown(
        '<div class="hero-subtitle">'
        'A business view of customer value, engagement and behavioral segments.'
        '</div>',
        unsafe_allow_html=True
    )

elif page == "Customers":
    st.title("Customer Explorer")
    st.markdown(
        '<div class="hero-subtitle">'
        "Explore an individual customer's RFM profile and business context."
        '</div>',
        unsafe_allow_html=True
    )

elif page == "Segments":
    st.title("Customer Segments")
    st.markdown(
        '<div class="hero-subtitle">'
        'Understand the size, value and strategic role of each customer segment.'
        '</div>',
        unsafe_allow_html=True
    )

else:
    st.title("Business Insights")
    st.markdown(
        '<div class="hero-subtitle">'
        'Key findings and actions derived from the customer segmentation analysis.'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# OVERVIEW
# ============================================================

if page == "Overview":

    st.markdown(
        '<div class="eyebrow">Portfolio Overview</div>',
        unsafe_allow_html=True
    )

    high_value = segment_summary[
        segment_summary["Segment"] == "High-Value Engaged"
    ].iloc[0]

    high_value_share = high_value["Customer_Share"]
    high_value_value_share = high_value["Value_Share"]

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.metric(
            "Customers",
            f"{total_customers:,}"
        )

    with k2:
        st.metric(
            "Purchase Value",
            f"£{total_purchase_value:,.0f}"
        )

    with k3:
        st.metric(
            "High-Value Customers",
            f"{int(high_value['Customers']):,}"
        )

    with k4:
        st.metric(
            "High-Value Share",
            f"{high_value_share:.1f}%"
        )

    st.write("")
    # ========================================================
    # VALUE CONCENTRATION
    # ========================================================

    with st.container(border=True):

        st.markdown(
            '<div class="eyebrow">Value Concentration</div>',
            unsafe_allow_html=True
        )

        c1, c2 = st.columns([0.9, 2.1], gap="large")

        with c1:

            st.metric(
                "Customer Share",
                f"{high_value_share:.1f}%"
            )

            st.caption(
                "High-Value Engaged customers"
            )

        with c2:

            st.subheader(
                f"{high_value_value_share:.1f}% of purchase value"
            )

            st.write(
                f"High-Value Engaged customers represent only "
                f"**{high_value_share:.1f}%** of the customer base "
                f"but generate **{high_value_value_share:.1f}%** "
                f"of total purchase value."
            )

            st.write(
                "**Priority:** Retention and relationship-building "
                "should focus on this group."
            )

    # Charts

    c1, c2 = st.columns(2)

    with c1:

        with st.container(border=True):

            st.markdown(
                '<div class="eyebrow">Customer Distribution</div>',
                unsafe_allow_html=True
            )

            chart_data = segment_summary.copy()

            chart = (
                alt.Chart(chart_data)
                .mark_bar(
                    cornerRadiusTopLeft=7,
                    cornerRadiusTopRight=7
                )
                .encode(
                    x=alt.X(
                        "Segment:N",
                        sort=segment_order,
                        axis=alt.Axis(
                            title=None,
                            labelAngle=-18
                        )
                    ),
                    y=alt.Y(
                        "Customers:Q",
                        axis=alt.Axis(
                            title="Customers",
                            grid=True
                        )
                    ),
                    color=alt.Color(
                        "Segment:N",
                        scale=alt.Scale(
                            domain=segment_order,
                            range=[
                                "#B0884D",
                                "#4F7A7C",
                                "#8EAFC0",
                                "#87908E"
                            ]
                        ),
                        legend=None
                    ),
                    tooltip=[
                        alt.Tooltip("Segment:N"),
                        alt.Tooltip("Customers:Q")
                    ]
                )
                .properties(
                    height=330
                )
            )

            st.altair_chart(
                chart,
                use_container_width=True
            )

    with c2:

        with st.container(border=True):

            st.markdown(
                '<div class="eyebrow">Purchase Value by Segment</div>',
                unsafe_allow_html=True
            )

            chart = (
                alt.Chart(chart_data)
                .mark_bar(
                    cornerRadiusTopLeft=7,
                    cornerRadiusTopRight=7
                )
                .encode(
                    x=alt.X(
                        "Segment:N",
                        sort=segment_order,
                        axis=alt.Axis(
                            title=None,
                            labelAngle=-18
                        )
                    ),
                    y=alt.Y(
                        "Purchase_Value:Q",
                        axis=alt.Axis(
                            title="Purchase Value",
                            format="~s",
                            grid=True
                        )
                    ),
                    color=alt.Color(
                        "Segment:N",
                        scale=alt.Scale(
                            domain=segment_order,
                            range=[
                                "#B0884D",
                                "#4F7A7C",
                                "#8EAFC0",
                                "#87908E"
                            ]
                        ),
                        legend=None
                    ),
                    tooltip=[
                        alt.Tooltip("Segment:N"),
                        alt.Tooltip(
                            "Purchase_Value:Q",
                            format=",.2f",
                            title="Purchase Value"
                        )
                    ]
                )
                .properties(
                    height=330
                )
            )

            st.altair_chart(
                chart,
                use_container_width=True
            )

    st.write("")

    # Segment performance

    with st.container(border=True):

        st.markdown(
            '<div class="eyebrow">Segment Performance</div>',
            unsafe_allow_html=True
        )

        display_summary = segment_summary.copy()

        display_summary["Customer Share"] = (
            display_summary["Customer_Share"].map(
                lambda x: f"{x:.1f}%"
            )
        )

        display_summary["Value Share"] = (
            display_summary["Value_Share"].map(
                lambda x: f"{x:.1f}%"
            )
        )

        display_summary["Purchase Value"] = (
            display_summary["Purchase_Value"].map(
                lambda x: f"£{x:,.0f}"
            )
        )

        display_summary["Avg Monetary"] = (
            display_summary["Avg_Monetary"].map(
                lambda x: f"£{x:,.2f}"
            )
        )

        display_summary = display_summary[
            [
                "Segment",
                "Customers",
                "Customer Share",
                "Purchase Value",
                "Value Share",
                "Avg Monetary"
            ]
        ]

        st.dataframe(
            display_summary,
            use_container_width=True,
            hide_index=True
        )

    st.write("")

    with st.container(border=True):

        st.markdown(
            '<div class="eyebrow">Executive Interpretation</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            The customer base is highly concentrated in value.

            **High-Value Engaged** customers account for only
            **{high_value_share:.1f}%** of customers while contributing
            **{high_value_value_share:.1f}%** of total purchase value.

            The combination of **High-Value Engaged** and
            **Moderate / Regular** customers represents approximately
            **43.3%** of the customer base and around **88.5%** of purchase
            value.

            This suggests that retention, relationship-building, upselling
            and cross-selling should receive greater strategic attention
            than broad untargeted campaigns.
            """
        )


# ============================================================
# CUSTOMERS
# ============================================================

elif page == "Customers":

    st.markdown(
        '<div class="eyebrow">Customer Profile</div>',
        unsafe_allow_html=True
    )

    customer_ids = sorted(df["CustomerID"].unique())

    selected_customer = st.selectbox(
        "Select a Customer ID",
        customer_ids,
        index=customer_ids.index(12346)
        if 12346 in customer_ids else 0,
        key="customer_explorer_id"
    )

    customer = df[
        df["CustomerID"] == selected_customer
    ].iloc[0]

    st.write("")

    with st.container(border=True):

        st.markdown(
            '<div class="eyebrow">Selected Customer</div>',
            unsafe_allow_html=True
        )

        st.metric(
            "Customer ID",
            f"{selected_customer:,}"
        )

    st.write("")

    st.markdown(
        '<div class="eyebrow">RFM Profile</div>',
        unsafe_allow_html=True
    )

    st.subheader("Customer RFM Profile")

    r1, r2, r3, r4 = st.columns(4)

    with r1:
        with st.container(border=True):
            st.metric(
                "Recency",
                f"{customer['Recency']:.0f} days"
            )

    with r2:
        with st.container(border=True):
            st.metric(
                "Frequency",
                f"{customer['Frequency']:.0f} invoice"
                if customer["Frequency"] == 1
                else f"{customer['Frequency']:.0f} invoices"
            )

    with r3:
        with st.container(border=True):
            st.metric(
                "Monetary Value",
                f"£{customer['Monetary']:,.2f}"
            )

    with r4:
        with st.container(border=True):
            st.metric(
                "RFM Score",
                f"{int(customer['RFM_Score'])}",
                help="RFM Score is a customer profile code created from Recency, Frequency and Monetary scores. It is not a numerical magnitude."
            )

    st.write("")

    selected_segment = customer["Segment"]

    segment_descriptions = {

        "High-Value Engaged":
            "Customers with very recent activity, strong repeat purchasing and high purchase value.",

        "Moderate / Regular":
            "Customers with moderate engagement and meaningful purchase value.",

        "Recent / Low-Frequency":
            "Customers who purchased recently but have not yet developed strong repeat purchasing behavior.",

        "Inactive / Low-Value":
            "Customers with low recent engagement, low purchasing frequency and relatively low purchase value."
    }

    segment_actions = {

        "High-Value Engaged":
            "Protect the relationship through retention, personalized recommendations, loyalty benefits and VIP treatment.",

        "Moderate / Regular":
            "Increase customer value through upselling, cross-selling, personalized recommendations and loyalty initiatives.",

        "Recent / Low-Frequency":
            "Encourage a second purchase using relevant recommendations, follow-up communication and low-friction offers.",

        "Inactive / Low-Value":
            "Use selective, low-cost reactivation campaigns while avoiding excessive acquisition or retention spend."
    }

    with st.container(border=True):

        s1, s2 = st.columns([1.1, 1])

        with s1:

            st.markdown(
                '<div class="eyebrow">Customer Segment</div>',
                unsafe_allow_html=True
            )

            st.subheader(selected_segment)

            st.write(
                segment_descriptions[selected_segment]
            )

        with s2:

            st.markdown(
                '<div class="eyebrow">Recommended Strategy</div>',
                unsafe_allow_html=True
            )

            st.write(
                segment_actions[selected_segment]
            )

    st.write("")

    # Customer interpretation

    with st.container(border=True):

        st.markdown(
            '<div class="eyebrow">Customer Interpretation</div>',
            unsafe_allow_html=True
        )

        recency = customer["Recency"]
        frequency = customer["Frequency"]
        monetary = customer["Monetary"]

        if selected_segment == "High-Value Engaged":

            interpretation = (
                f"This customer is highly valuable and actively engaged, "
                f"with a recent purchase history, approximately "
                f"{frequency:.0f} invoice-based purchases and "
                f"£{monetary:,.2f} in purchase value. "
                f"Retention and relationship-building should be prioritized."
            )

        elif selected_segment == "Moderate / Regular":

            if frequency <= 2 and recency > 180:

                interpretation = (
                    f"This customer has a high purchase value of "
                    f"£{monetary:,.2f}, but has made only "
                    f"{frequency:.0f} invoice-based purchase and has not "
                    f"purchased for {recency:.0f} days. Although the customer "
                    f"is classified as Moderate / Regular by the clustering "
                    f"model, the actual profile suggests a high-value "
                    f"customer who could benefit from targeted reactivation "
                    f"and relationship-building."
                )

            elif frequency <= 2:

                interpretation = (
                    f"This customer has meaningful purchase value of "
                    f"£{monetary:,.2f}, but relatively limited repeat "
                    f"purchasing with {frequency:.0f} invoice-based "
                    f"purchase(s). The opportunity is to encourage "
                    f"additional purchases and strengthen the relationship."
                )

            else:

                interpretation = (
                    f"This customer shows moderate-to-strong purchasing "
                    f"behavior, with {frequency:.0f} invoice-based purchases "
                    f"and £{monetary:,.2f} in purchase value. "
                    f"The main opportunity is to increase customer value "
                    f"through upselling, cross-selling and loyalty initiatives."
                )

        elif selected_segment == "Recent / Low-Frequency":

            interpretation = (
                f"This customer purchased recently, with a recency of "
                f"{recency:.0f} days, but has made only "
                f"{frequency:.0f} invoice-based purchase(s). "
                f"The strongest opportunity is to convert recent activity "
                f"into repeat purchasing."
            )

        else:

            interpretation = (
                f"This customer has relatively low engagement, with "
                f"{recency:.0f} days since the most recent purchase, "
                f"{frequency:.0f} invoice-based purchase(s), and "
                f"£{monetary:,.2f} in purchase value. "
                f"Selective and cost-conscious reactivation is more "
                f"appropriate than intensive retention investment."
            )

        st.write(interpretation)


# ============================================================
# SEGMENTS
# ============================================================

elif page == "Segments":

    st.markdown(
        '<div class="eyebrow">Segment Portfolio</div>',
        unsafe_allow_html=True
    )

    st.subheader("Segment Overview")

    cards = [
        (
            "High-Value Engaged",
            "green-card"
        ),
        (
            "Moderate / Regular",
            "blue-card"
        ),
        (
            "Recent / Low-Frequency",
            "purple-card"
        ),
        (
            "Inactive / Low-Value",
            "gold-card"
        )
    ]

    cols = st.columns(4)

    for col, (segment, card_class) in zip(cols, cards):

        row = segment_summary[
            segment_summary["Segment"] == segment
        ].iloc[0]

        with col:

            with st.container(border=True):

                st.markdown(
                    f'<div class="eyebrow">{segment}</div>',
                    unsafe_allow_html=True
                )

                st.metric(
                    "Customers",
                    f"{int(row['Customers']):,}"
                )

                st.write(
                    f"**{row['Customer_Share']:.1f}%** of customers"
                )

                st.write(
                    f"**{row['Value_Share']:.1f}%** of purchase value"
                )

    st.write("")

    # Size vs value

    c1, c2 = st.columns(2)

    with c1:

        with st.container(border=True):

            st.markdown(
                '<div class="eyebrow">Customer Share</div>',
                unsafe_allow_html=True
            )

            chart = (
                alt.Chart(segment_summary)
                .mark_bar(
                    cornerRadiusTopLeft=7,
                    cornerRadiusTopRight=7
                )
                .encode(
                    x=alt.X(
                        "Segment:N",
                        sort=segment_order,
                        axis=alt.Axis(
                            title=None,
                            labelAngle=-18
                        )
                    ),
                    y=alt.Y(
                        "Customer_Share:Q",
                        axis=alt.Axis(
                            title="Customer Share (%)"
                        )
                    ),
                    color=alt.Color(
                        "Segment:N",
                        scale=alt.Scale(
                            domain=segment_order,
                            range=[
                                "#B0884D",
                                "#4F7A7C",
                                "#8EAFC0",
                                "#87908E"
                            ]
                        ),
                        legend=None
                    ),
                    tooltip=[
                        alt.Tooltip("Segment:N"),
                        alt.Tooltip(
                            "Customer_Share:Q",
                            format=".1f",
                            title="Customer Share"
                        )
                    ]
                )
                .properties(height=320)
            )

            st.altair_chart(
                chart,
                use_container_width=True
            )

    with c2:

        with st.container(border=True):

            st.markdown(
                '<div class="eyebrow">Value Share</div>',
                unsafe_allow_html=True
            )

            chart = (
                alt.Chart(segment_summary)
                .mark_bar(
                    cornerRadiusTopLeft=7,
                    cornerRadiusTopRight=7
                )
                .encode(
                    x=alt.X(
                        "Segment:N",
                        sort=segment_order,
                        axis=alt.Axis(
                            title=None,
                            labelAngle=-18
                        )
                    ),
                    y=alt.Y(
                        "Value_Share:Q",
                        axis=alt.Axis(
                            title="Purchase Value Share (%)"
                        )
                    ),
                    color=alt.Color(
                        "Segment:N",
                        scale=alt.Scale(
                            domain=segment_order,
                            range=[
                                "#B0884D",
                                "#4F7A7C",
                                "#8EAFC0",
                                "#87908E"
                            ]
                        ),
                        legend=None
                    ),
                    tooltip=[
                        alt.Tooltip("Segment:N"),
                        alt.Tooltip(
                            "Value_Share:Q",
                            format=".1f",
                            title="Value Share"
                        )
                    ]
                )
                .properties(height=320)
            )

            st.altair_chart(
                chart,
                use_container_width=True
            )

    st.write("")

    # RFM characteristics

    with st.container(border=True):

        st.markdown(
            '<div class="eyebrow">RFM Characteristics</div>',
            unsafe_allow_html=True
        )

        rfm_table = segment_summary[
            [
                "Segment",
                "Avg_Recency",
                "Avg_Frequency",
                "Avg_Monetary"
            ]
        ].copy()

        rfm_table["Avg Recency"] = (
            rfm_table["Avg_Recency"].map(
                lambda x: f"{x:.1f} days"
            )
        )

        rfm_table["Avg Frequency"] = (
            rfm_table["Avg_Frequency"].map(
                lambda x: f"{x:.1f} invoices"
            )
        )

        rfm_table["Avg Monetary"] = (
            rfm_table["Avg_Monetary"].map(
                lambda x: f"£{x:,.2f}"
            )
        )

        rfm_table = rfm_table[
            [
                "Segment",
                "Avg Recency",
                "Avg Frequency",
                "Avg Monetary"
            ]
        ]

        st.dataframe(
            rfm_table,
            use_container_width=True,
            hide_index=True
        )

    st.write("")

    # Business interpretation

    st.markdown(
        '<div class="eyebrow">Business Interpretation</div>',
        unsafe_allow_html=True
    )

    business_cards = {

        "High-Value Engaged": (
            "Protect the relationship",
            "These customers are the strongest value contributors. "
            "Focus on retention, VIP treatment, personalized recommendations, "
            "early access and loyalty benefits."
        ),

        "Moderate / Regular": (
            "Grow customer value",
            "This group shows meaningful activity and represents an "
            "important middle-value opportunity. Focus on upselling, "
            "cross-selling and personalized recommendations."
        ),

        "Recent / Low-Frequency": (
            "Create the second purchase",
            "These customers are recent but have weak repeat behavior. "
            "The main objective is converting recent activity into "
            "a stronger customer relationship."
        ),

        "Inactive / Low-Value": (
            "Reactivate selectively",
            "This group has low engagement and low purchase value. "
            "Use low-cost, selective reactivation rather than expensive "
            "retention campaigns."
        )
    }

    cols = st.columns(2)

    for index, segment in enumerate(segment_order):

        row = segment_summary[
            segment_summary["Segment"] == segment
        ].iloc[0]

        title, text = business_cards[segment]

        with cols[index % 2]:

            with st.container(border=True):

                st.markdown(
                    f'<div class="eyebrow">{segment}</div>',
                    unsafe_allow_html=True
                )

                st.subheader(title)

                st.write(text)

                st.caption(
                    f"{int(row['Customers']):,} customers • "
                    f"{row['Customer_Share']:.1f}% of customers • "
                    f"{row['Value_Share']:.1f}% of purchase value"
                )

        if index % 2 == 1:
            st.write("")

    # Management priority

    st.write("")

    with st.container(border=True):

        st.markdown(
            '<div class="eyebrow">Management Priority</div>',
            unsafe_allow_html=True
        )

        priority_col1, priority_col2 = st.columns(2)

        with priority_col1:

            st.metric(
                "Customer Share",
                "43.3%"
            )

        with priority_col2:

            st.metric(
                "Value Share",
                "88.5%"
            )

        st.markdown(
            """
            **High-Value Engaged + Moderate / Regular** customers represent
            approximately **43.3% of the customer base** but contribute around
            **88.5% of total purchase value**.

            These customers should receive the strongest relationship-building,
            retention, upselling and cross-selling attention.

            **Recent / Low-Frequency** represents a future growth opportunity,
            while **Inactive / Low-Value** should generally be approached with
            cost-conscious reactivation strategies.
            """
        )


# ============================================================
# INSIGHTS
# ============================================================

else:

    st.markdown(
        '<div class="eyebrow">Executive Summary</div>',
        unsafe_allow_html=True
    )

    high_value = segment_summary[
        segment_summary["Segment"] == "High-Value Engaged"
    ].iloc[0]

    moderate = segment_summary[
        segment_summary["Segment"] == "Moderate / Regular"
    ].iloc[0]

    recent = segment_summary[
        segment_summary["Segment"] == "Recent / Low-Frequency"
    ].iloc[0]

    inactive = segment_summary[
        segment_summary["Segment"] == "Inactive / Low-Value"
    ].iloc[0]

    st.subheader("Executive Snapshot")

    with st.container(border=True):

        st.markdown(
            f"""
            ### Customer value is highly concentrated

            Only **{high_value['Customer_Share']:.1f}%** of customers belong
            to the **High-Value Engaged** segment, yet they generate
            **{high_value['Value_Share']:.1f}%** of total purchase value.

            The next priority is the **Moderate / Regular** group, which
            represents **{moderate['Customer_Share']:.1f}%** of customers and
            contributes **{moderate['Value_Share']:.1f}%** of value.

            Together, these two groups form the core economic base of the
            customer portfolio.
            """
        )

    st.write("")

    # Four insights

    insight_data = [

        (
            "01",
            "Protect high-value customers",
            f"{int(high_value['Customers']):,} customers generate "
            f"{high_value['Value_Share']:.1f}% of purchase value.",
            "Retention and relationship-building should be prioritized."
        ),

        (
            "02",
            "Grow the middle",
            f"{int(moderate['Customers']):,} customers contribute "
            f"{moderate['Value_Share']:.1f}% of purchase value.",
            "Upselling, cross-selling and loyalty initiatives can increase value."
        ),

        (
            "03",
            "Convert recent customers",
            f"{int(recent['Customers']):,} customers are recent but "
            f"remain low-frequency.",
            "The key objective is encouraging a second purchase."
        ),

        (
            "04",
            "Reactivate selectively",
            f"{int(inactive['Customers']):,} customers are classified as "
            f"Inactive / Low-Value.",
            "Use cost-conscious reactivation rather than intensive retention."
        )
    ]

    cols = st.columns(2)

    for i, (
        number,
        title,
        body,
        action
    ) in enumerate(insight_data):

        with cols[i % 2]:

            with st.container(border=True):

                st.markdown(
                    f'<div class="eyebrow">Insight {number}</div>',
                    unsafe_allow_html=True
                )

                st.subheader(title)

                st.write(body)

                st.caption(
                    f"Action: {action}"
                )

        if i % 2 == 1:
            st.write("")

    st.write("")

    # Business priorities

    with st.container(border=True):

        st.markdown(
            '<div class="eyebrow">Business Priorities</div>',
            unsafe_allow_html=True
        )

        priorities = [
            (
                "1",
                "Retention",
                "Protect High-Value Engaged customers through strong relationships and loyalty."
            ),
            (
                "2",
                "Expansion",
                "Increase Moderate / Regular customer value through upselling and cross-selling."
            ),
            (
                "3",
                "Conversion",
                "Move Recent / Low-Frequency customers toward repeat purchasing."
            ),
            (
                "4",
                "Efficiency",
                "Keep Inactive / Low-Value reactivation campaigns selective and low-cost."
            )
        ]

        for number, title, text in priorities:

            p1, p2 = st.columns([0.12, 0.88])

            with p1:
                st.markdown(
                    f"### {number}"
                )

            with p2:
                st.markdown(
                    f"**{title}**  \n{text}"
                )

            st.divider()

    # RFM takeaway

    st.write("")

    with st.container(border=True):

        st.markdown(
            '<div class="eyebrow">RFM Takeaway</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
            **Recency** helps identify how recently customers purchased.

            **Frequency** identifies repeat purchasing behavior.

            **Monetary** captures customer purchase value.

            Combining these dimensions with K-Means clustering produces
            customer groups that can be interpreted from a business
            perspective rather than relying only on a single score.
            """
        )

    st.write("")

    # Analytics note

    with st.container(border=True):

        st.markdown(
            '<div class="eyebrow">Analytics Note</div>',
            unsafe_allow_html=True
        )

        st.write(
            "The final segmentation uses K-Means clustering on log-transformed "
            "and standardized RFM variables. Four clusters were selected "
            "because they provided a useful balance between analytical "
            "quality and business actionability."
        )


