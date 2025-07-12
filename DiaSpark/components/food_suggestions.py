import gradio as gr

def render_food_guide():
    """
    Creates and returns the Gradio UI for the 'Healthy Eating Guide'.
    """
    with gr.Blocks() as food_ui:
        gr.Markdown("## 🥗 Healthy Eating Guide for Diabetes Management")
        gr.Markdown(
            "A healthy diet is one of the most powerful tools for managing and preventing diabetes. "
            "Focus on whole, nutrient-dense foods."
        )
        gr.Markdown("---")

        with gr.Row():
            with gr.Column(scale=2):
                gr.Markdown("### Foods to Embrace 🍏")
                gr.Markdown(
                    """
                    *   **🥬 Leafy Greens:** Spinach, kale, and collards are low in calories and carbohydrates but high in vitamins and minerals.
                    *   **🍓 Berries:** Strawberries, blueberries, and raspberries are packed with antioxidants, vitamins, and fiber.
                    *   **🐟 Fatty Fish:** Salmon, sardines, and mackerel are excellent sources of omega-3 fatty acids, which are great for heart health.
                    *   **🥜 Nuts & Seeds:** Almonds, walnuts, and chia seeds provide healthy fats, fiber, and protein.
                    *   **🌾 Whole Grains:** Quinoa, oats, and brown rice are better than refined grains as they have less impact on blood sugar.
                    *   **豆 Legumes:** Beans, lentils, and chickpeas are high in fiber and protein, helping you feel full and stabilizing blood sugar.
                    """
                )
            with gr.Column(scale=1):
                gr.Markdown("### Foods to Limit 🍔")
                gr.Markdown(
                    """
                    *   **🥤 Sugary Drinks:** Soda, sweetened teas, and fruit juices.
                    *   **🍞 White Bread & Pasta:** These are refined carbs that can spike blood sugar.
                    *   **🍟 Fried Foods:** Often high in unhealthy fats and calories.
                    *   **🍰 Packaged Sweets:** Cakes, cookies, and pastries are high in sugar and unhealthy fats.
                    *   **🥩 Processed Meats:** Sausages and bacon can be high in sodium and unhealthy fats.
                    """
                )
        
        gr.Markdown("---")
        gr.Markdown(
            "💡 **Pro Tip:** Portion control is a key! Use smaller plates and be mindful of serving sizes. "
            "For personalized advice, always consult with a registered dietitian or your healthcare provider."
        )