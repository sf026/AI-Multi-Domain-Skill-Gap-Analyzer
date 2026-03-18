def resume_improver(missing_skills):

    suggestions = []

    for skill in missing_skills[:10]:
        suggestions.append(
            f"Add projects or experience related to {skill}"
        )

    suggestions.append("Add measurable achievements")
    suggestions.append("Use ATS-friendly keywords")

    return suggestions