"""
QUESTION:
Create a function `generate_training_report` that takes in the following parameters: `phase`, `loss_per_epoch`, `mse_per_epoch`, `clip_grad_D`, `grad_norm_D`, `clip_grad_S`, `grad_norm_S`. The function should return a formatted report containing the following information for the specified phase: 
- Total loss
- Likelihood
- KL divergence for Gaussian distributions
- KL divergence for the inferred Gaussian
- Mean squared error (MSE) per epoch
- Gradient norms and clipping thresholds for the discriminator and the generator. 

The function should handle the given parameters and return a string that represents the report. The report should be well-structured and easy to read.
"""

def generate_training_report(phase, loss_per_epoch, mse_per_epoch, clip_grad_D, grad_norm_D, clip_grad_S, grad_norm_S):
    report = f"Training Report for {phase} phase:\n"
    report += f"Total Loss: {loss_per_epoch['Loss']}\n"
    report += f"Likelihood: {loss_per_epoch['lh']}\n"
    report += f"KL Divergence for Gaussian Distributions: {loss_per_epoch['KLG']}\n"
    report += f"KL Divergence for Inferred Gaussian: {loss_per_epoch['KLIG']}\n"
    report += f"Mean Squared Error (MSE) per Epoch: {mse_per_epoch[phase]}\n"
    report += f"Gradient Norm for Discriminator (D): {grad_norm_D}, Clipping Threshold: {clip_grad_D}\n"
    report += f"Gradient Norm for Generator (S): {grad_norm_S}, Clipping Threshold: {clip_grad_S}\n"
    return report