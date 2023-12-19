import streamlit as st
from re_gpt import SyncChatGPT

session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..6QZRgOrIdhdSqUbc.70O9sB7xNu74TQ9DPmeEg_Hjcfr9uB9pK7tN9FtNOon-plIU5a1OfIDqU1xFru5ZlDx_DTeBXQ6PkK4aouzlbIZg5WJwONTeHqTSHBS1Qn2jvrVbZ-05dYaIMfyE1J6zyPiUFTFHJKZnx7QrDzaF818jN0n2FMOyzq3jCtudp_cIrv33h9gnPS091q5MPXXPfEKiyYghDKpLDufPfBs0AjBQeftPrNIss-DqcIzdjDvUlZkSHnbe0FZVfryKrOuL6xw_Tll0-s5v4vb87zBN26zuvLJsx6_J1QFgOKW_OR1JWl-eeJ52MEohcJ0D0O-MkxLDlKMCXSW3VtIAZTnH3m4xv_44CVOTU8IVUDhFvndrz2X1RW9AfKKFyjmExdkit6yF9ooCV_XPj3UMsLp3y4XB94VSICabxixFYwfozxmsTUtCr_8BwKZHYLMonUEjc4dThupUgXGNPVrpAjxw4-6GPKy5yQ-URSZNIDYOt5ZJvaTuGoJkOM4pyynDUmu3OvxHqnUugrl7dVr_nsg1jgMoPIGA2g8FCowV5F-lUq8uDw4olBQPbSmzNhCGyoQASpH_hIgVaiwpBMzS0ssqOq4h1fN2PfAatynUxcRpnSlII-cr0TiVmtJxyDc_bKEdIkbsP8598cVxG87XUGC8DYrlw7ThpIjdHa_LkpFuYXxVSMQOgbLc5Z6qK02N6PugExEBpkVzXuq6D1l6W7y3y0H-3AYaVDyCMwPpI6lAGFbs5ANsMtDXcc-P_JrRGZG2Lu9KC0VyyRwxT8KdnlIAOxTDg_8EvsBxQUG_MlhmrPQzeSYAPDyg8ME45jsnEkYiRXRzuoYPLAKbRrALMppbDtaBW_2aJ7INaK626YsMmXdHGBHhe11cy_cCEbaRApaDbdxRsqEgXInD4j2Q-OkSC5h-6JreuEMHW4tcnMxvFnQXH8iAUqbYSAZPrNPSxb3mrjOeqrSlxrEX39r54kO4a_pqwpFK0qgk3HS8E72Xx7FK0_HouCzEaukdMSyP29RgvSrZOrDYIRBmbyNOPDaF0vZ1CMBXvLohlUtmA0mForzf7w9613a_TPFxJ9GGQvwqqoROgAgB3IXAP8f6ibEgxgIIwJgY8d4lyZs-rdp7JSicodJ66adVtPzbhNxD-fWF_zPksVoXb45lVu37dbBKWMdyd3F7KoUwtptbjCcQD8tOQ91cH9kLakxjm3iHP2N2e3L-PbASSkIeRrtLfv1lAHS4MtTGY3YhmT1wBVcwO2czjKAgwEVhsJK4LCJd_gYTuKljJxDz0epytgMcZI8zyGql91_9sIylKm80Mrvobu3x1kqfaij8Gh2mSAGJz1p90_cQkwcoJexeOT1aLH3w4W8PqfEfQCNAsu30h1xCaRnViIp2QT75D_lO_aKQd-FKvBhnT6q37zjMyqrfK_tgYWr6jV4KgzyZqthfrqhIYiofBKxVpzMjRd-7cJ_aWefW7GdkBc3t5pBU44IfvKHqrHmjRIjtV-CEVHYbryXUPijsbHTiUX0NbvSIdW9NUWGBPKaXNIfwRJ4tPixbfOvOW2zYZVIdZJ1KdKwF1swFkjBJzfKDo_8u6uRCjhMEqPVvb-dxnbAereTRLTtpeefj-OpH7kYn14dTJGqyFTh13YEvruAKtILjcaucxqxZ0gHsjcecTUjEKZsLf8MMacig_z97S3UPd3Mob3bwRR_9ALx7Ze8aVywJzraPY__VuBbskFV0irl7flR6AdLfy5xs1RHiPYkvKSyKTF6NNe18B1ctc4MwpEjimrAcALUYwayPpENpjE5WGVhI-LL5WqbropHY2xWcqCGKV7oIPyzGoc9q9Y5quW91_QqlkWdRPTFyHbDme12fmpvK7T4dOzpLPLw2U51pXYRU2_5TZga8ne4zzZti0hFZoqM-LZZYxjPxdWZ7V7kXDOb2i1sIWqWWr1wayKNdKoukBgu85EObRYLAyV5sBPTGdaEHFx9bJGcXNF1_yBB05Y0MXvHkyJxEdQCvAltw4HDd1lueX_Ct5m4V7niv4uKrqy57qQIUeEQ1GhtTL5MokJ18JFFq_hpgqpyAc2zE5bcbuVKxTb5K_j3vtkOLEXTx4jqj81WZiinrK-4BWRLM8xXNt5VymzAemydQFQjfPdudYfW4X-PXR9d8UQmmo70wxba6PdhwA0WGIKLDjFcbYNPGj5xDtOenTY-m-SAE-PoRv40GWglmm2NEN7k3g3_k24VqlxJ4vOXiSwY76vJj-7RqdLrjd7B6w4nq4JLCTN65zQD6wxnOMrugXmqeR-2RG8YlnZJYMNxcISgc8VpMFpBmBPpm3YLZEH6UBHyRBZO1XylYsdI7QX2ABuNM-2qFFWHKgBV3PJV744c7srbJ7sPDSqTrTW3VDFjrV0U84BxOoKgE7EZ6s9nLJ4P3X-miSm15tTuMVQrl5rjJmIOd-oc0Qxau8J5jdHOeS4_0qEFFONyYTcQh06v6HiscokXoF4joYRGYhZfX8amtEIYi5Ics02nP83-pWyWbDDAXwVi-bTCSTYPrpVbijIysqQkLEVpm3BMRKrrIFkV6XEUMqqCQQLnpHFa2of-9mTUCCfvko_8tggd-z9UAtEZTf1mJZYbU4MFdfVoZqgyxt_XE2VubfuAtg_qP5DyTINWalJhnHtc3audpxlD9yLMPLaMX-lOjBXqhly6ApXGIMLRel5hhmfkmsGf-vJ9KeSKeLhpqIgGo22KQABBl1VXizMQHD2Uh_sqBhqdgtqVkV17LsyKrzS_FCg3q0uJhNxIKyUcqPijV3Pw0GO8HwtaL5PsGPOaRdlyuAIXKmQ.UKQpHpZChX09cRU0iAVvtA"
conversation_id = None # conversation ID here

# Function to summarize text based on learning rate
def summarize_text(prompt, learning_rate):
    if learning_rate == 0.5:
        summary_prompt = f"Summarize the following text in points:\n\n{prompt}\n\nwith a neutral learning rate of 0.5."
    elif learning_rate < 0.5:
        summary_prompt = f"Summarize the following text in points:\n\n{prompt}\n\nwith a layman's understanding (learning rate: {learning_rate})."
    else:
        summary_prompt = f"Summarize the following text in points:\n\n{prompt}\n\nwith a more complex and concise explanation (learning rate: {learning_rate})."
    with SyncChatGPT(session_token=session_token) as chatgpt:
        if conversation_id:
            conversation = chatgpt.get_conversation(conversation_id)
        else:
            conversation = chatgpt.create_new_conversation()

        summary = ""
        for message in conversation.chat(summary_prompt):
            summary += message["content"]

        return summary

# Streamlit app
def main():
    st.title("Text Summarization with Learning Rate")

    # User input prompt
    prompt = st.text_area("Enter your text:")

    # Learning rate slider
    learning_rate = st.slider("Select Learning Rate", 0.0, 1.0, 0.5, 0.01)

    # Summarize button
    if st.button("Summarize Text"):
        # Summarize text based on learning rate
        summary = summarize_text(prompt, learning_rate)

        # Display the summarized text
        st.subheader("Summarized Text:")
        st.write(summary)

if __name__ == "__main__":
    main()
