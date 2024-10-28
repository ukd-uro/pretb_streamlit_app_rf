def convert_to_text(output):
    psma_string = "Bevorzugt PSMA-PET-CT. Alternativ Ganzkörperknochenszintigraphie und CT-Abdomen und Becken. "
    ct_string = "CT Abdomen und Becken. "
    scintigraphy_string = "Ganzkörperknochenszintigraphie. "
    as_string = "Der Patient erfüllt die Kriterien für eine aktive Überwachung. Falls eine definitive Therapie erwünscht ist, Angebot einer radikalen Prostatektomie oder alternativ perkutane Strahlentherapie."
    rp_string = "Indikation zur radikalen Prostatektomie."
    rt_string = "Perkutane Strahlentherapie."
    
    ct_scintigraphy_string = "Ganzkörperknochenszintigraphie und CT-Abdomen und Becken. "
    
    output_string = ""
    
    if output[0] == 1:
        # PSMA
        output_string += psma_string

    if output[1] == 1:
        # CT
        if output[0] == 0:
            if output[2] == 1:
                output_string += ct_scintigraphy_string
            else:
                output_string += ct_string

    if output[2] == 1:
        # Scintigraphy
        if output[0] == 0:
            if output[1] ==1:
                output_string += ct_scintigraphy_string
            else:
                output_string += scintigraphy_string

    if output[3] == 1:
        # Active surveillance
        output_string += as_string

    if output[4] == 1:
        # Radical prostatectomy
        if output[3] == 0:
            output_string += rp_string

    if output[5] == 1:
        # Radiation therapy
        if output[3] == 0:
            if output[4] == 1:
                output_string += " Alternativ " + rt_string
            else:
                output_string += rt_string
    
    return output_string